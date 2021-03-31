# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy

# Lecture de l'image
img_color = cv2.imread('Meduse.jpg',cv2.IMREAD_COLOR)
plt.subplot(331),plt.imshow(img_color)
plt.title(''), plt.xticks([]), plt.yticks([])

# Inversion des composantes R et B
img = deepcopy(img_color)
img[:,:,0] = img_color[:,:,2]
img[:,:,2] = img_color[:,:,0]
img[0,0,:]=[0,0,0] # premier pixel noir
img[0,1,:]=[255,255,255] # second pixel blanc
plt.subplot(332),plt.imshow(img)
plt.title('RGB'), plt.xticks([]), plt.yticks([])

# Affichage des histogrammes
plt.subplot(334),plt.hist(img[:,:,0].ravel(), bins=256);
plt.title('Histogram R'), plt.xticks([]), plt.yticks([])
plt.subplot(335),plt.hist(img[:,:,1].ravel(), bins=256);
plt.title('Histogram G'), plt.xticks([]), plt.yticks([])
plt.subplot(336),plt.hist(img[:,:,2].ravel(), bins=256);
plt.title('Histogram B'), plt.xticks([]), plt.yticks([])

# Affichage de certaines valeurs de pixels
print('blue : ' )
print(img[55, 63])
print('dark blue : ' )
print(img[82, 939])
print('orange : ' )
print(img[356, 318])
print('dark orange : ' )
print(img[276, 212])
print('red : ' )
print(img[449, 438])

# Creation du masque pour la segmentation par couleur
lower_blue = np.array([0,0,0])
upper_blue = np.array([10,255,255])
mask = cv2.inRange(img, lower_blue, upper_blue)

# Creation de l'image en fausses couelurs
image_fausses_couleurs = np.zeros(img.shape)
image_fausses_couleurs[:,:,0] = mask.astype(int)*255
image_fausses_couleurs[:,:,1] = mask.astype(int)*255
image_fausses_couleurs[:,:,2] = mask.astype(int)*255

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= cv2.bitwise_not(mask))

# Affichage des images
plt.subplot(337),plt.imshow(img)
plt.title('Initial Image'), plt.xticks([]), plt.yticks([])
plt.subplot(338),plt.imshow(res)
plt.title('Segmented Image 1'), plt.xticks([]), plt.yticks([])
plt.subplot(339),plt.imshow(image_fausses_couleurs)
plt.title('Segmented Image 2'), plt.xticks([]), plt.yticks([])
plt.show()
  
