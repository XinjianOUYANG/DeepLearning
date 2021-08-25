import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from rich.console import Console
from rich.table import Table
from functools import partial
import sys
import os
from pathlib import Path
sys.path.append(str(Path(os.path.abspath(__file__)).parent.parent))
from utils import *

class KDTree: # kd树类
    class Node: # 节点类
        def __init__(self, points, labels, axis):
            self.points = points    # x
            self.labels = labels    # y
            self.axis = axis  # 点所在坐标轴
            self.left = None
            self.right = None

    def build(self, X, Y, layer = 0): # 构造kd树
        if not len(X):
            return None
        k = X.shape[1]
        split_axis = layer % k
        median_ind = np.argpartition(X[:, split_axis], len(X) // 2, axis=0)[-1] # argpartition 从小到大排序，[-1]表示取第一大的值
        ''''
        def argpartition(a, kth, axis=-1, kind='introselect', order=None):
        
            Perform an indirect partition along the given axis using the
        algorithm specified by the `kind` keyword. It returns an array of
        indices of the same shape as `a` that index data along the given
        axis in partitioned order.
        '''
        split_point = float(X[median_ind, split_axis]) # 分岔点
        equal_x = X[X[:, split_axis] == split_point] # 分界线上的点
        equal_y = Y[X[:, split_axis] == split_point]
        less_x = X[X[:, split_axis] < split_point]
        less_y = Y[X[:, split_axis] < split_point]
        greater_x = X[X[:, split_axis] > split_point]
        greater_y = Y[X[:, split_axis] > split_point]
        node = self.Node(equal_x, equal_y, split_axis)
        node.left = self.build(less_x, less_y, layer+1)
        node.right = self.build(greater_x, greater_y, layer+1)

        return node

    def __init__(self, X, Y):
        self.root = self.build(X, Y)

    def _query(self, root, x, k): #搜索kd树 search root
        if not root:
            return Heap(max_len=k, key=lambda xy: -euc_dis(x, xy[0])), inf  # heap 优先队列结构
        mindis = inf
        # Find the region that contains the target point
        if x[root.axis] <= root.points[0][root.axis]: #从根结点出发递归
            ans, lmindis = self._query(root.left, x, k)
            mindis = min(mindis, lmindis)
            sibling = root.right #姊妹节点，for other_ans...
        else:
            ans, rmindis = self._query(root.right, x, k)
            mindis = min(mindis, rmindis)
            sibling = root.left
        # All the points on the current splitting line are possible answers
        for curx, cury in zip(root.points, root.labels):
            mindis = min(euc_dis(curx, x), mindis)
            ans.push((curx, cury))
        # If the distance between the target point and the splitting line is
        # shorter than the best answer up until, find the other tree
        if mindis > abs(x[root.axis] - root.points[0][root.axis]):  # the distance between hyperplane
            other_ans, other_mindis = self._query(sibling, x, k)
            mindis = min(mindis, other_mindis)
            while other_ans: # ans = True
                otherx, othery = other_ans.pop() # 出队列
                ans.push((otherx, othery)) #入队列
        return ans, mindis

    def query(self, x, k):
        return self._query(self.root, x, k)[0]


class KNN: # ensemble KNN
    def __init__(self, k=1, distance_func="l2"):
        self.k = k
        if distance_func == 'l2':
            self.distance_func = lambda x, y: np.linalg.norm(x - y)
        else:
            self.distance_func = distance_func

    def fit(self, X, Y):
        self.tree = KDTree(X, Y) # fit data
        self.k = min(self.k, len(X))

    def _predict(self, x):
        topk = self.tree.query(x, self.k)
        topk_y = [y for x, y in topk] #分类
        return np.argmax(np.bincount(topk_y))

    def predict(self, X):
        return np.apply_along_axis(self._predict, axis=-1, arr=X)

if __name__ == "__main__":
    def demonstrate(X_train, Y_train, X_test, k, desc):
        knn = KNN(k=k)
        knn.fit(X_train, Y_train)
        pred_test = knn.predict(X_test) # KNN 分类测试
        print(knn.tree.Node)

        # plot
        plt.scatter(X_train[:,0], X_train[:,1], c=Y_train, s=20)
        plt.scatter(X_test[:,0], X_test[:,1], c=pred_test, marker=".", s=1)
        plt.title(desc)
        plt.show()

    # -------------------------- Example 1 ----------------------------------------
    X_train = np.array([[2, 3], [5,4 ], [9, 6], [4, 7], [8, 1], [7,2]])
    Y_train = np.array([1, 2, 3, 4, 5, 6])
    # generate grid-shaped test data
    X_test = np.concatenate(np.stack(np.meshgrid(np.linspace(-1, 2, 100), np.linspace(-1, 2, 100)), axis=-1))
    demonstrate(X_train, Y_train, X_test, 1, "Example 1")

    # X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1], [.5, .5]])
    # Y_train = np.array([1, 2, 3, 4, 5])
    # # generate grid-shaped test data
    # X_test = np.concatenate(np.stack(np.meshgrid(np.linspace(-1, 2, 100), np.linspace(-1, 2, 100)), axis=-1))
    # demonstrate(X_train, Y_train, X_test, 1, "Example 1")
    #
    # # -------------------------- Example 2 (Imbalanced Data) ------------------------
    # X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1], [.5, .5]])
    # Y_train = np.array([1, 1, 2, 3, 4])
    # # generate grid-shaped test data
    # X_test = np.concatenate(np.stack(np.meshgrid(np.linspace(-1, 2, 100), np.linspace(-1, 2, 100)), axis=-1))
    # demonstrate(X_train, Y_train, X_test, 1, "Example 2")
    #
    # # -------------------------- Example 3 (Imbalanced Data) ------------------------
    # X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1], [.5, .5]])
    # Y_train = np.array([1, 1, 2, 2, 2])
    # # generate grid-shaped test data
    # X_test = np.concatenate(np.stack(np.meshgrid(np.linspace(-1, 2, 100), np.linspace(-1, 2, 100)), axis=-1))
    # demonstrate(X_train, Y_train, X_test, 1, "Example 3")
