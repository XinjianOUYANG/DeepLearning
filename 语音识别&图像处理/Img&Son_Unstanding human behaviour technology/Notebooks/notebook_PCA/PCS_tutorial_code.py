###Computing the covariance matrix

from sklearn.preprocessing import StandardScaler
X = StandardScaler().fit_transform(X) #X is dataset

import numpy as np

# # Compute the mean of the data
# mean_vec = np.mean(X, axis=0)

# # Compute the covariance matrix
# cov_mat = (X - mean_vec).T.dot((X - mean_vec)) / (X.shape[0]-1)

# OR we can do this with one line of numpy:
cov_mat = np.cov(X.T)

###Computing Eigen Values and Vectors

# Compute the eigen values and vectors using numpy
eig_vals, eig_vecs = np.linalg.eig(cov_mat)

# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort(key=lambda x: x[0], reverse=True)

###Projection onto new vectors
# Only keep a certain number of eigen vectors based on 
# the "explained variance percentage" which tells us how 
# much information (variance) can be attributed to each of the principal components

exp_var_percentage = 0.97 # Threshold of 97% explained variance

tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)

num_vec_to_keep = 0

for index, percentage in enumerate(cum_var_exp):
  if percentage > exp_var_percentage:
    num_vec_to_keep = index + 1
    break


# Compute the projection matrix based on the top eigen vectors
num_features = X.shape[1]
proj_mat = eig_pairs[0][1].reshape(num_features,1)
for eig_vec_idx in range(1, num_vec_to_keep):
  proj_mat = np.hstack((proj_mat, eig_pairs[eig_vec_idx][1].reshape(num_features,1)))

# Project the data 
pca_data = X.dot(proj_mat)

# https://www.dezyre.com/data-science-in-python-tutorial/principal-component-analysis-tutorial
“”“

    step1: Normalize the data
    step2: Calculate the covatiance matrix
    step3: Calculate the eigenvalues and eigenvectors
    step4: Choosing components and forming a feature vector
    step5: Forming principal components: NewData = FeatureVector^T x ScaledData^T

”“”