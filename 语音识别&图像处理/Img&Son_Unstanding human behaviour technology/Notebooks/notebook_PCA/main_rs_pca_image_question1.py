# -*- coding: utf-8 -*-
"""
Created on Mon Oct 07 16:20:54 2013

@author: rseguier

https://realpython.com/python-keras-text-classification/

"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA    # inital reduction
from sklearn.manifold import TSNE                   # final reduction
import numpy as np

Base_dir_yes = "..\\data\\yes\\"
Base_dir_no = "..\\data\\no\\"


img_right_no = mpimg.imread(Base_dir_no + "im000.bmp")
img_left_no = mpimg.imread(Base_dir_no + "im019.bmp")
img_up_yes = mpimg.imread(Base_dir_yes + "im017.bmp")
img_down_yes = mpimg.imread(Base_dir_yes + "im035.bmp")
img_central_no = mpimg.imread(Base_dir_no + "im010.bmp")
img_central_yes = mpimg.imread(Base_dir_yes + "im007.bmp")
SizeX = img_right_no.shape[0]
SizeY = img_right_no.shape[1]

def PCA_base_creation(Base_dir_name):
    vect_database = []
    for ii in range(500):
        # print(ii)
        try:
            File_name = Base_dir_name + "im" + str(ii).zfill(3) + ".bmp"
            print(File_name)
            img = mpimg.imread(File_name)
            size = SizeX*SizeY
            print(size)
            vect = img.reshape(size)

            vect_database.append(vect)
        except:
            break;
    return vect_database

# number of Eigen vectors you are going to evaluate
num_dimensions = 10
BaseTrain_yes = PCA_base_creation(Base_dir_yes)
BaseTrain_no = PCA_base_creation(Base_dir_no)
#BaseTest = PCA_base_creation(Base_dir_no)

PCA_YesorNo = PCA(n_components=num_dimensions)
#PCA_YesorNo.fit(BaseTrain_yes)
PCA_YesorNo.fit(BaseTrain_no)

# display the mean
MeanVectYes = PCA_YesorNo.mean_

# display the eigen vectors
EigenVect = PCA_YesorNo.components_

#Vect2display = EigenVect[0] + MeanVect
"""
Vect2display = EigenVect[0]
Eigen_image = Vect2display.reshape(SizeX, SizeY)
fig = plt.figure() # create a new figure window
img_grid = fig.add_subplot(1, 1, 1)
img_grid.imshow(Eigen_image, cmap='gray') 
plt.show()
"""
NbIm = 19
# ImgToProject = BaseTrain_yes[NbIm].reshape(SizeX, SizeY)
ImgToProject = BaseTrain_no[NbIm].reshape(SizeX, SizeY)

# Vect_projected = PCA_YesorNo.transform(BaseTrain_yes)
Vect_projected = PCA_YesorNo.transform(BaseTrain_no)
#Vect_projected = PCA_YesorNo.transform(np.transpose(VectToProject))
reconstructVect = PCA_YesorNo.inverse_transform(Vect_projected)


Image_reconstr = reconstructVect[NbIm, :].reshape(SizeX, SizeY)

fig = plt.figure() # create a new figure window
img_grid = fig.add_subplot(2, 1, 1)
plt.title("original")
img_grid.imshow(ImgToProject, cmap='gray')
img_grid = fig.add_subplot(2, 1, 2)
plt.title("reconstructed")
img_grid.imshow(Image_reconstr, cmap='gray')


plt.show()