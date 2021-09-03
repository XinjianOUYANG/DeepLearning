from ast import literal_eval
from matplotlib import pyplot as plt
import numpy as np
import sys
import os
from pathlib import Path
sys.path.append(str(Path(os.path.abspath(__file__)).parent.parent))
from utils import binary_cross_entropy, sigmoid, wbline

# 回归/分类模型
class LogisticRegression:
    def __init__(self, `lr`=1e-4, max_steps=1000, verbose=True):
        self.lr = lr
        self.max_steps = max_steps
        self.verbose = verbose

    def fit(self, X, Y):
        """
        X: of shape [data-size, feature-size]
        Y: of shape [data-size]
        """
        self.feature_size = X.shape[-1]
        # w of shape [feature-size]
        self.w = np.random.rand(self.feature_size) # 随机赋值
        # b of shape [1]
        self.b = np.random.rand(1)

        for step in range(self.max_steps):
            # pred of shape [data-size]
            pred = self._predict(X)
            # 梯度下降法, 计算梯度表达式！！
            # https://zhuanlan.zhihu.com/p/44591359
            # Bias gradient of shape [data-size]
            gradient_b = Y - pred
            # Weight gradient of shape [data-size, feature-size]
            gradient_w = gradient_b[:, None] * X
            # get mean of gradient across all data
            gradient_b = gradient_b.mean(axis=0)
            gradient_w = gradient_w.mean(axis=0)
            self.w += gradient_w * self.lr
            self.b += gradient_b * self.lr
            loss = binary_cross_entropy(pred, Y) 
            if self.verbose:
                print(f"Step {step}, Loss is {loss}...")

    def _predict(self, X):
        logit = self.w @ X.T + self.b
        p = sigmoid(logit)
        '''
        def sigmoid(x):
            return 1 / (np.exp(-x) + 1)
        '''
        return p

    def predict(self, X):
        p = self._predict(X)
        Y = (p > .5).astype(int)
        return Y

if __name__ == "__main__":
    def demonstrate(X, Y, desc):
        logistic_regression = LogisticRegression(verbose=True)
        logistic_regression.fit(X, Y)

        # plot
        plt.title(desc)
        plt.scatter(X[:, 0], X[:, 1], c=Y)
        wbline(logistic_regression.w, logistic_regression.b)
        plt.show()

    # -------------------------- Example 1 ----------------------------------------
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    Y = np.array([1, 1, 0, 0])
    demonstrate(X, Y, "Example 1")

    # -------------------------- Example 2 ----------------------------------------
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    Y = np.array([1, 0, 0, 1])
    demonstrate(X, Y, "Example 2: Logistic Regression still cannot solve a simple XOR problem")

    # -------------------------- Example 3 ----------------------------------------
    X = np.concatenate([np.random.normal([0, 1], size=[40, 2]),
                        np.random.normal([1, 0], size=[40, 2])])
    Y = np.concatenate([np.ones(40), np.zeros(40)])
    demonstrate(X, Y, "Example 3: Logistic Regression is suitable for tasks that are not strictly linear separable")
