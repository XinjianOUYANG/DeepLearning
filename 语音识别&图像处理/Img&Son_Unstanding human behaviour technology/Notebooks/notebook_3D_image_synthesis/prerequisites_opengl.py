from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import cv2
 
'''
OpenGL:
    https://zhuanlan.zhihu.com/p/56693625
    OpenGL（Open Graphics Library）是一个跨编程语言、跨平台的编程图形程序接口，
    它将计算机的资源抽象称为一个个OpenGL的对象，
    对这些资源的操作抽象为一个个的OpenGL指令。
'''

# window display size
GLB_width, GLB_height = 400, 400
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
    gluPerspective(45.0, faspect,5, 130.0)
    '''
    gluPerspective = platform.createBaseFunction( 
    'gluPerspective', dll=platform.PLATFORM.GLU, resultType=None, 
    argTypes=[GLdouble,GLdouble,GLdouble,Ldouble],
    doc='gluPerspective( GLdouble(fovy), GLdouble(aspect), GLdouble(zNear), GLdouble(zFar) ) -> None', 
    argNames=('fovy', 'aspect', 'zNear', 'zFar'),
    )   
    '''
    # camera Position
    # http://pyopengl.sourceforge.net/documentation/manual-3.0/gluLookAt.html
    gluLookAt(0.0, 0.0, -6.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    

def display():
    
    # we clean the display buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # we act on the object referential
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()
    # glTranslatef()
    # glRotatef()

    glBegin(GL_TRIANGLE_STRIP)
    Utext = 55.0 / GLB_large_text
    Vtext = 162.0 / GLB_haut_text
    glTexCoord2f(Utext,Vtext)
    # specifying the color of each vertex
    # V0
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    # V1
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    # V2
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.0, 0.0, 0.0)
    # V3
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(0.0, 0.0, -1.0)
    # V4
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glEnd()

    # we force the execution all the commands
    glFlush()
    # on swap les buffer de sorties et de travail
    glutSwapBuffers()
    # we force the display
    glutPostRedisplay()


# Keyboard management
def keyboard( key, x, y ):
    if key == b'\x1b' or key==b"q":
        sys.exit(0)

def keyboard_simple(key,x,y):
    key_in_str = key.decode('utf-8')
    print(key_in_str)


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
