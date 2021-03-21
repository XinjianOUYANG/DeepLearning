import os
import numpy as np
from matplotlib import pyplot as plt
from rich.console import Console
from rich.table import Table
import sys
from pathlib import Path
sys.path.append(str(Path(os.path.abspath(__file__)).parent.parent))
from utils import *


class Perceptron:
    def __init__(self, lr=1e-1, max_iteration=2000, verbose=False):
        self.lr = lr # learning rate
        self.verbose = verbose #详细模式
        self.max_iteration = max_iteration

    def gram(self, X):
        self.N = len(X)
        self.G = np.zeros((self.N,self.N))
        for i in np.arange(self.N):
            for j in np.arange(self.N):
                self.G[i,j] = X[i].T @ X[j]
        return self.G 

    def _trans(self, i, G, Y):
        return self.alpha.T * Y @ G[i].T + self.b # @ matrix multiply

    def _predict(self, i, G, Y):
        return 1 if self._trans(i, G, Y) >= 0. else -1

    def fit(self, X, Y):
        self.N = len(X)
        # define parameteres randomly
        self.alpha = np.zeros((self.N,1))
        self.b = 0
        self.G = self.gram(X)

        updated = 1
        epoch = 0
        # if there is mis-classified sample, train
        while updated > 0 and epoch < self.max_iteration:
            if self.verbose:
                print(f"epoch {epoch} started...")  

            updated = 0
            # shuffle data 随机打乱顺序
            #perm = np.random.permutation(self.N)
            for i in np.arange(self.N):
                y = Y[i]
                # if there is a mis-classified sample 错分类项
                if self._predict(i,self.G,Y) != y:
                    print(i,self._predict(i,self.G,Y),y)
                    # update the parameters, minimize loss function(gradient method)
                    self.alpha[i] += self.lr
                    self.b += self.lr * y
                    updated += 1
            print(self.alpha,self.b)

            if self.verbose:
                print(f"epoch {epoch} finishied, {updated} pieces of data mis-classified")
            epoch += 1

        self.w = (self.alpha.T * Y @ X).T
        return

    def predict(self, X):
        return np.apply_along_axis(self._predict, axis=-1, arr=X)

def demonstrate(X, Y, desc):
    console = Console(markup=False)
    perceptron = Perceptron(lr = 1,verbose=True)
    perceptron.fit(X, Y)

    # plot
    plt.scatter(X[:, 0], X[:, 1], c=Y)
    wbline(perceptron.w, perceptron.b)
    plt.title(desc)
    plt.show()

    G = perceptron.G
    N = perceptron.N
    # show in table
    pred = [perceptron._predict(i,G,Y) for i in np.arange(N)]
    table = Table('x', 'y', 'pred')
    for x, y, y_hat in zip(X, Y, pred):
        table.add_row(*map(str, [x, y, y_hat]))
    console.print(table)

# -------------------------- Example 1 ----------------------------------------
print("Example 1:")
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([1, 1, -1, -1])
demonstrate(X, Y, "Example 1")

# -------------------------- Example 2 ----------------------------------------
# print("Example 2: Perceptron cannot solve a simple XOR problem")
# X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Y = np.array([1, -1, -1, 1])
# demonstrate(X, Y, "Example 2: Perceptron cannot solve a simple XOR problem")

