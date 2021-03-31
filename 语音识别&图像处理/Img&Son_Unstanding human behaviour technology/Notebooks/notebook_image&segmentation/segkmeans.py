# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt
from copy import copy, deepcopy

plt.close('all')

img_tmp = cv2.imread("Meduse.jpg", cv2.IMREAD_COLOR)
img = deepcopy(img_tmp)
img[:,:,0] = img_tmp[:,:,2]
img[:,:,2] = img_tmp[:,:,0]
img_hsv = img
img_gray = cv2.imread("Meduse.jpg",cv2.IMREAD_GRAYSCALE)
Z = img_hsv.reshape((-1,3))
print(len(Z))
print(np.size(Z))
print(len(img))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

print(len(label))
print(len(center))
print(center)
center = [[255, 255, 255], [0, 0, 0] ]

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

plt.figure()
plt.subplot(221),plt.imshow(img_hsv)
plt.title('Initial'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_gray,cmap=plt.cm.gray)
plt.subplot(224),plt.hist(img_gray.ravel(),256,[0,256]);     
plt.subplot(222),plt.imshow(res2)
plt.title('Segmented'), plt.xticks([]), plt.yticks([])
plt.show()




