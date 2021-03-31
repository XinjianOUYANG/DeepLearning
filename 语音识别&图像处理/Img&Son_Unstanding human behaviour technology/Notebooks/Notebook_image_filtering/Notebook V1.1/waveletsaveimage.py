# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy



#-------------------------------
# FUNCTIONS
#-------------------------------
# Convolution in one direction
def convOneDirection (img, kernel) :
    h = len(kernel)//2
    img_conv = np.zeros(img.shape)
    for i in range (0, len(img)):
        for j in range(h, len(img[0])-h):
            sum=0
            for m in range(len(kernel)):
                sum=sum+kernel[m]*img[i][j-h+m]
            img_conv[i][j] = sum
    return img_conv

# Downsampling in one direction
def downsamplOneDirection(img,firstPoint): 
    img_downsampl = np.zeros((len(img), len(img[0])//2))
    for i in range (0, len(img)):
        for j in range (0, len(img[0])//2):
            img_downsampl[i][j] = img[i][2*j+firstPoint]
    return img_downsampl

# Upsampling in one direction
def upsamplOneDirection(img,firstPoint): 
    img_upsubsampl = np.zeros((len(img), len(img[0])*2))
    for i in range (0, len(img)):
        for j in range (0, len(img[0])):
            img_upsubsampl[i][j*2+firstPoint] = img[i][j]
    return img_upsubsampl

# Mirror the matrix
def mirrorMatrix(img):
    img_miror = np.zeros((len(img[0]), len(img)))
    for i in range (0, len(img[0])):
        for j in range(0, len(img)):
            img_miror[i][j] = img[j][i]
    return img_miror



class usefullDwtFunctions:

    # Decomposition
    @staticmethod #静态方法
    def decomposition(img):
        print("")
        print("Image with max amplitude : " + str(np.max(img)))
        print("Starting decomposition...")
        kernelL = [-1, 2, 6, 2, -1] # coefMult*[-1, 2, 6, 2, -1]/8
        kernelH = [-4, 8, -4] # coefMult*[-1, 2, -1]/2
        firstPointL = 0 # first pixel for low pass filters
        firstPointH = 1 # second pixel for high pass filters

        imgL = downsamplOneDirection(convOneDirection(img, kernelL), firstPointL) # LossPass Filter on width + downsample by 2
        imgLcopy = mirrorMatrix(deepcopy(imgL))
        imgLL = mirrorMatrix(downsamplOneDirection(convOneDirection(imgLcopy, kernelL), firstPointL)) # LossPass Filter on height + downsample by 2
        imgLH = mirrorMatrix(downsamplOneDirection(convOneDirection(imgLcopy, kernelH), firstPointH)) # HighPass Filter on height + downsample by 2
        imgH = downsamplOneDirection(convOneDirection(img, kernelH), firstPointH) # LossPass Filter on width + downsample by 2
        imgHcopy = mirrorMatrix(deepcopy(imgH))
        imgHL = mirrorMatrix(downsamplOneDirection(convOneDirection(imgHcopy, kernelL), firstPointL)) # LossPass Filter on height + downsample by 2
        imgHH = mirrorMatrix(downsamplOneDirection(convOneDirection(imgHcopy, kernelH), firstPointH)) # HighPass Filter on height + downsample by 2

        print("Decommposition finished")
        print("Max amplitude of integer images are : " + str(np.max(img)) + " (0 filter), " + str(np.max(imgL))+ " " + str(np.max(imgH))+ " (1 filter), " + str(np.max(imgLL))+ " " + str(np.max(imgLH))+ " " + str(np.max(imgHL))+ " " + str(np.max(imgHH)) + " (2 filters)")
        print("Min amplitude of integer images are : " + str(np.min(img)) + " (0 filter), " + str(np.min(imgL))+ " " + str(np.min(imgH))+ " (1 filter), " + str(np.min(imgLL))+ " " + str(np.min(imgLH))+ " " + str(np.min(imgHL))+ " " + str(np.min(imgHH)) + " (2 filters)")
        print("The images are " + str(len(imgLL[0])) + " pixels wide and " + str(len(imgLL)) + " pixels high.")
        return [imgLL, imgLH, imgHL, imgHH]

    # Reconstruction
    @staticmethod
    def reconstruction(imgLL, imgLH, imgHL, imgHH):
        print("")
        print("Starting recontruction...")
        kernelH = [-1, -2, 6, -2, -1] # coefMult*[-1, -2, 6, -2, -1]/8
        kernelL = [4, 8, 4] # coefMult*[1, 2, 1]/2
        firstPointL = 0 # first pixel for low pass filters
        firstPointH = 1 # second pixel for high pass filters

        imgRL1 = convOneDirection(upsamplOneDirection(mirrorMatrix(imgLL),firstPointL), kernelL)
        imgRL2 = convOneDirection(upsamplOneDirection(mirrorMatrix(imgLH),firstPointH), kernelH)
        imgRL = mirrorMatrix(imgRL1+imgRL2)
        imgRH1 = convOneDirection(upsamplOneDirection(mirrorMatrix(imgHL),firstPointL), kernelL) 
        imgRH2 = convOneDirection(upsamplOneDirection(mirrorMatrix(imgHH),firstPointH), kernelH) 
        imgRH = mirrorMatrix(imgRH1+imgRH2)
        imgR1 = convOneDirection(upsamplOneDirection(imgRL,firstPointL), kernelL)
        imgR2 = convOneDirection(upsamplOneDirection(imgRH,firstPointH), kernelH)
        imgR = imgR1 + imgR2

        print("Reconstruction finished")
        print("Max amplitude of integer images are : " + str(np.max(imgLL))+ " " + str(np.max(imgLH))+ " " + str(np.max(imgHL))+ " " + str(np.max(imgHH)) + " (0 filter), " + str(np.max(imgRL1)) + " " + str(np.max(imgRL2))+ " " + str(np.max(imgRH1))+ " " + str(np.max(imgRH2))+ " " + str(np.max(imgRL))+ " " + str(np.max(imgRH))+ " (1 filter) " + str(np.max(imgR1))+ " " + str(np.max(imgR2))+ " " + str(np.max(imgR)) + " (2 filters)")
        print("Min amplitude of integer images are : " + str(np.min(imgLL))+ " " + str(np.min(imgLH))+ " " + str(np.min(imgHL))+ " " + str(np.min(imgHH)) + " (0 filter), " + str(np.min(imgRL1)) + " " + str(np.min(imgRL2))+ " " + str(np.min(imgRH1))+ " " + str(np.min(imgRH2))+ " " + str(np.min(imgRL))+ " " + str(np.min(imgRH))+ " (1 filter) " + str(np.min(imgR1))+ " " + str(np.min(imgR2))+ " " + str(np.min(imgR)) + " (2 filters)")
        print("The image is " + str(len(imgR[0])) + " pixels wide and " + str(len(imgR)) + " pixels high.")
        return imgR


    # Verification
    @staticmethod
    def verification(img, titleimg, imgR, titleimgR, edge):
        print("")
        print("Starting verification...")
        imgCropped = img[edge:len(img)-edge, edge:len(img[0])-edge]
        imgRCropped = imgR[edge:len(img)-edge, edge:len(img[0])-edge]
        plt.subplot(1,3,1),plt.imshow(imgCropped, cmap = 'gray'),plt.title(titleimg), plt.xticks([]), plt.yticks([])
        plt.subplot(1,3,2),plt.imshow(imgRCropped, cmap = 'gray'),plt.title(titleimgR), plt.xticks([]), plt.yticks([])
        maskVerif = np.abs((img-imgR)[edge:len(img)-edge, edge:len(img[0])-edge]) # difference between the 2 images, without the edges 
        deltaValue = np.max(maskVerif)
        print("Mask delta value : " + str(deltaValue) )
        maskVerif[0][0] = 0; maskVerif[0][1] = 255 # to avoid min-max equalization from matplotlib :)
        plt.subplot(1,3,3),plt.imshow(maskVerif, cmap = 'gray'),plt.title('Reconstruction error'), plt.xticks([]), plt.yticks([])
        plt.show()

