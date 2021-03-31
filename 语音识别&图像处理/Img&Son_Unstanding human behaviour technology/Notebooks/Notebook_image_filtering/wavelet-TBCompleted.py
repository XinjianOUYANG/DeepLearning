# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy


img = cv2.imread('imsynth.bmp',cv2.IMREAD_GRAYSCALE) # read the image
#img = cv2.imread('Lena.bmp',cv2.IMREAD_GRAYSCALE) # read the image
print("")
print("The image is " + str(len(img[0])) + " pixels wide and " + str(len(img)) + " pixels high.")

#-------------------------------
# FUNCTIONS
#-------------------------------
# 1.1 Convolution in one direction
def convOneDirection (img, kernel) :
    h = len(kernel)//2
    img_conv = np.zeros(img.shape)
    for i in range (0, len(img)):
        for j in range(h, len(img[0])-h):
            TBC
            img_conv[i][j] = TBC
    return img_conv

# 1.2 Downsampling in one direction
def downsamplOneDirection(img,firstPoint): 
    img_downsampl = np.zeros((len(img), len(img[0])//2))
    TBC
    return img_downsampl

# 2.1 Upsampling in one direction
def upsamplOneDirection(img,firstPoint): 
    img_upsubsampl = np.zeros((len(img), len(img[0])*2))
    for i in range (0, len(img)):
        for j in range (0, len(img[0])):
            img_upsubsampl[i][j*2+firstPoint] = img[i][j]
    return img_upsubsampl

# 1.3 Mirror the matrix
def mirrorMatrix(img):
    img_miror = np.zeros((len(img[0]), len(img)))
    for i in range (0, len(img[0])):
        for j in range(0, len(img)):
            img_miror[i][j] = img[j][i]
    return img_miror


#-------------------------------
# 1.1 FILTRERING IN ONE DIRECTION
#-------------------------------
print("")
img_comp_lowpassfilter = convOneDirection (img, [-1, 2, 6, 2, -1]) 
img_comp_highpassfilter = convOneDirection (img, [-2, 4, -2]) 
plt.subplot(1,3,1),plt.imshow(img, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(img_comp_lowpassfilter, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(img_comp_highpassfilter, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.show()

#-------------------------------
# 1.2 DOWNSAMPLE IN ONE DIRECTION
#-------------------------------
print("")
img_comp_lowpassfilter = downsamplOneDirection (img_comp_lowpassfilter, 0) 
img_comp_highpassfilter = downsamplOneDirection (img_comp_highpassfilter, 1) 
plt.subplot(1,2,1),plt.imshow(img, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(1,4,3),plt.imshow(img_comp_lowpassfilter, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(1,4,4),plt.imshow(img_comp_highpassfilter, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.show()

#-------------------------------
# 1.3 DECOMPOSITION
#-------------------------------
# Decomposition
print("")
print("Image with max amplitude : " + str(np.max(img)))
print("Starting decomposition...")
coefMult = 8 # to keep integer for computation
kernelL = [-1, 2, 6, 2, -1] # coefMult*[-1, 2, 6, 2, -1]/8
kernelH = [-4, 8, -4] # coefMult*[-1, 2, -1]/2
firstPointL = 0 # first pixel for low pass filters
firstPointH = 1 # second pixel for high pass filters

imgL = TBC
imgLcopy = mirrorMatrix(deepcopy(imgL))
imgLL = TBC
imgLH = TBC
imgH = TBC
imgHcopy = mirrorMatrix(deepcopy(imgH))
imgHL = TBC
imgHH = TBC

print("Decommposition finished")
print("Max amplitude of integer images are : " + str(np.max(img)) + " " + str(np.max(imgL))+ " " + str(np.max(imgH))+ " " + str(np.max(imgLL))+ " " + str(np.max(imgLH))+ " " + str(np.max(imgHL))+ " " + str(np.max(imgHH)))
print("The images are " + str(len(imgLL[0])) + " pixels wide and " + str(len(imgLL)) + " pixels high.")

plt.subplot(1,4,1),plt.imshow(img, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(2,8,3),plt.imshow(imgL, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(2,8,11),plt.imshow(imgH, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(4,8,4),plt.imshow(imgLL, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(4,8,12),plt.imshow(imgLH, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(4,8,20),plt.imshow(imgHL, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(4,8,28),plt.imshow(imgHH, cmap = 'gray'), plt.xticks([]), plt.yticks([])

#-------------------------------
# 2.1 RECONSTRUCTION
#-------------------------------
# Reconstruction
print("")
print("Starting recontruction...")
kernelH = [-1, -2, 6, -2, -1] # coefMult*[-1, -2, 6, -2, -1]/8
kernelL = [4, 8, 4] # coefMult*[1, 2, 1]/2
irstPointL = 0 # first pixel for low pass filters
firstPointH = 1 # second pixel for high pass filters

imgRL1 = TBC
imgRL2 = TBC
imgRL = mirrorMatrix(imgRL1+imgRL2)
imgRH1 = TBC
imgRH2 = TBC 
imgRH = mirrorMatrix(imgRH1+imgRH2)
imgR1 = TBC
imgR2 = TBC
imgR = imgR1 + imgR2
plt.subplot(2, 8, 6),plt.imshow(imgRL, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 8, 14),plt.imshow(imgRH, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 4, 4),plt.imshow(imgR, cmap = 'gray'), plt.xticks([]), plt.yticks([])
print("Reconstruction finished")
print("Max amplitude of integer images are : " + str(np.max(imgRL1)) + " " + str(np.max(imgRL2))+ " " + str(np.max(imgRH1))+ " " + str(np.max(imgRH2))+ " " + str(np.max(imgRL))+ " " + str(np.max(imgRH))+ " " + str(np.max(imgR1))+ " " + str(np.max(imgR2))+ " " + str(np.max(imgR)))
print("The image is " + str(len(imgR[0])) + " pixels wide and " + str(len(imgR)) + " pixels high.")
plt.show()

#-------------------------------
# 2.2 VERIFICATION
#-------------------------------
imgR = imgR//coefMult**4 # coefMult**4 is due to the fact that we keep integers before - see kernel values
print("")
print("Starting verification...")
edge = 3
maskVerif = TBC
print("Mask delta value : " + str(np.max(maskVerif)) )
maskVerif[0][0] = 0; maskVerif[0][1] = 255 # to avoid min-max equalization from matplotlib :)
plt.imshow(maskVerif, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.show()