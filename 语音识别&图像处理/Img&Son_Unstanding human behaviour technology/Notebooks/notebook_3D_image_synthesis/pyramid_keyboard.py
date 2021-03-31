# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import cv2

# window display size
GLB_width, GLB_height = 400, 400
# rotation angle
GLB_angle_rotation = 15.0
# pyramid coordinates
GLB_X, GLB_Y, GLB_Z = 0, 1, 0
# profondeur initiale des pyramides
GLB_Z_Depart=50
# texture
GLB_large_text,GLB_haut_text = 256, 256


def init():
    # we clean the output buffer
    glClearColor(0.0, 0.0, 0.0, 0.0)
    # we accept color interpolation
    glShadeModel(GL_SMOOTH)
    # we specify depth test
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    LoadTexture()


def LoadTexture():
    pMatrice = cv2.imread('im.bmp')
    textID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D,textID)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,GLB_large_text,GLB_haut_text,0,GL_RGB,GL_UNSIGNED_BYTE,pMatrice)
    
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # projection perspective
    faspect = w/h

    # (voir p582 ref.manual Opengl1.2)
    # have a look at
    # http://pyopengl.sourceforge.net/documentation/manual-3.0/gluPerspective.html
    gluPerspective(45.0, faspect, 5.0, 130.0)
    # camera Position
    # http://pyopengl.sourceforge.net/documentation/manual-3.0/gluLookAt.html
    gluLookAt(0.0, 0.0, -6.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    

def display():
    global GLB_angle_rotation, GLB_X, GLB_Y, GLB_Z

    # we clean the display buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # we act on the object referential
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # Translation
    glTranslatef(GLB_X, GLB_Y, GLB_Z)
    # object rotation
    glRotatef(GLB_angle_rotation, 1, 1, 1)

    glBegin(GL_TRIANGLE_STRIP)
    # # V0
    # glColor3f(1.0, 0.0, 0.0)
    # glVertex3f(-1.0, 0.0, 0.0)
    # # V1
    # glColor3f(0.0, 1.0, 0.0)
    # glVertex3f(0.0, 1.0, 0.0)
    # # V2
    # glColor3f(0.0, 0.0, 1.0)
    # glVertex3f(1.0, 0.0, 0.0)
    # # V3
    # glColor3f(0.0, 1.0, 1.0)
    # glVertex3f(0.0, 0.0, -1.0)
    # # V4
    # glColor3f(1.0, 0.0, 0.0)
    # glVertex3f(-1.0, 0.0, 0.0)
    # glEnd()
    Utext = 55.0 / GLB_large_text
    Vtext = 162.0 / GLB_haut_text
    glTexCoord2f(Utext,Vtext)
    glVertex3f(1.0, 0.0, 0.0)
    # V1
    Utext = 184.0 / GLB_large_text
    Vtext = 162.0 / GLB_haut_text
    glTexCoord2f(Utext, Vtext)
    glVertex3f(-1, 0.0, 0.0)
    # V2
    Utext = 119.0 / GLB_large_text
    Vtext = 13.0 / GLB_haut_text
    glTexCoord2f(Utext, Vtext)
    glVertex3f(0.0, 1, 0.0)
    glEnd()

    # we force the execution all the commands
    glFlush()
    # on swap les buffer de sorties et de travail1
    glutSwapBuffers()
    # we force the display
    glutPostRedisplay()

def keyboard_simple(key, x, y):
    key_in_str = key.decode('utf-8')
    print(key_in_str)

def keyboard(key, x, y):
    global GLB_angle_rotation, GLB_X, GLB_Y, GLB_Z
    key_in_str = key.decode('utf-8')
    if key_in_str == '2':
        GLB_Y = GLB_Y - 1
    if key_in_str == '8':
        GLB_Y = GLB_Y + 1
    # we force the display
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(GLB_width, GLB_height)
glutInitWindowPosition(100, 100)
glutCreateWindow('TD OpenGL CentraleSupelec')
# function d'initialisation
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
# Infinite loop: order management
glutMainLoop()
