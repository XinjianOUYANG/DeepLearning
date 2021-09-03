import numpy as np
from math import nan, inf
from pprint import pprint
from rich.console import Console
from rich.table import Table
from collections import Counter
import sys
import os
from pathlib import Path
sys.path.append(str(Path(os.path.abspath(__file__)).parent.parent))
from utils import gini

# 分类CART：特征选择，树的生成，剪枝
class ClassificationCART:
    class Node:
        def __init__(self, col, Y):
            self.col = col
            self.val = None
            self.left, self.right = None, None
            self.label = Counter(Y).most_common(1)[0][0]

    def __init__(self, verbose=False):
        self.verbose = verbose

    # 计算Gini系数 
    def get_gini_of_split(self, Y1, Y2):
        """get the square error of a split"""
        # Assume that we assign each a certain label to the two set,
        # the best assignment is the mean value of each set
        gini1 = gini(Y1)
        gini2 = gini(Y2)
        length = len(Y1) + len(Y2)
        return len(Y1) / length * gini1 + len(Y2) / length * gini2

    def build(self, X, Y):
        cur = self.Node(None, Y)
        if self.verbose:
            print("Cur data:")
            pprint(X)
            print(Y)
        best_gini = inf
        best_col, best_val = -1, nan
        # The book doesn't discuss about when to cease.
        # So I take the easiest way: cease when the data cannot be splitted
        if len(set(Y)) > 1: # 不是单结点树
            for col in range(len(X[0])):
                val_set = set(X[:, col])
                if len(val_set) != 1: # 特征数 > 1
                    for val in val_set:
                        # Don't split by the minimal value
                        # because no value is smaller than it
                        # so the left part is empty
                        # 根据‘是’、‘否’将数据机分成两个部分
                        selected_ind = X[:, col] == val
                        other_ind = X[:, col] != val
                        selected_Y = Y[selected_ind]
                        other_Y = Y[other_ind]
                        cur_gini = self.get_gini_of_split(selected_Y, other_Y)
                        if cur_gini < best_gini:
                            best_gini, best_col, best_val = cur_gini, col, val

            # Build left and right child nodes recursively
            print(f"Split by value {best_val} of {best_col}th column")
            selected_ind = X[:, best_col] == best_val
            other_ind = X[:, best_col] != best_val
            selected_X = X[selected_ind]
            other_X = X[other_ind]
            selected_Y = Y[selected_ind]
            other_Y = Y[other_ind]

            cur.col = best_col
            cur.val = best_val
            cur.left = self.build(selected_X, selected_Y)
            cur.right = self.build(other_X, other_Y)
        elif self.verbose:
            print("No split")
        return cur

    def query(self, root, x):
        if root.col is None:
            return root.label
        elif x[root.col] != root.val:
            return self.query(root.right, x)
        return self.query(root.left, x)

    def fit(self, X, Y):
        self.root = self.build(X, Y)

    def _predict(self, x):
        return self.query(self.root, x)

    def predict(self, X):
        return [self._predict(x) for x in X]

if __name__ == "__main__":
    console = Console(markup=False)
    cart = ClassificationCART(verbose=True)
    # -------------------------- Example 1 ----------------------------------------
    print("Example 1:")
    X = np.array([
        ['青年', '否', '否', '一般'],
        ['青年', '否', '否', '好'],
        ['青年', '是', '否', '好'],
        ['青年', '是', '是', '一般'],
        ['青年', '否', '否', '一般'],
        ['老年', '否', '否', '一般'],
        ['老年', '否', '否', '好'],
        ['老年', '是', '是', '好'],
        ['老年', '否', '是', '非常好'],
        ['老年', '否', '是', '非常好'],
        ['老年', '否', '是', '非常好'],
        ['老年', '否', '是', '好'],
        ['老年', '是', '否', '好'],
        ['老年', '是', '否', '非常好'],
        ['老年', '否', '否', '一般'],
    ])
    Y = np.array(['否', '否', '是', '是', '否', '否', '否', '是', '是', '是', '是', '是', '是', '是', '否'])
    cart.fit(X, Y)

    # show in table
    pred = cart.predict(X)
    table = Table('x', 'y', 'pred')
    for x, y, y_hat in zip(X, Y, pred):
        table.add_row(*map(str, [x, y, y_hat]))
    console.print(table)

    # -------------------------- Example 2 ----------------------------------------
    # but unpruned decision tree doesn't generalize well for test data
    print("Example 2:")
    X = np.array([
        ['青年', '否', '否', '一般'],
        ['青年', '否', '否', '好'],
        ['青年', '是', '是', '一般'],
        ['青年', '否', '否', '一般'],
        ['老年', '否', '否', '一般'],
        ['老年', '否', '否', '好'],
        ['老年', '是', '是', '好'],
        ['老年', '否', '是', '非常好'],
        ['老年', '否', '是', '非常好'],
        ['老年', '否', '是', '非常好'],
        ['老年', '否', '是', '好'],
        ['老年', '否', '否', '一般'],
    ])
    Y = np.array(['否', '否', '是', '否', '否', '否', '是', '是', '是', '是', '是', '否'])
    cart.fit(X, Y)

    testX = np.array([
        ['青年', '否', '否', '一般'],
        ['青年', '否', '否', '好'],
        ['青年', '是', '否', '好'],
        ['青年', '是', '是', '一般'],
        ['青年', '否', '否', '一般'],
        ['老年', '否', '否', '一般'],
        ['老年', '否', '否', '好'],
        ['老年', '是', '是', '好'],
        ['老年', '否', '是', '非常好'],
        ['老年', '否', '是', '非常好'],
        ['老年', '否', '是', '非常好'],
        ['老年', '否', '是', '好'],
        ['老年', '是', '否', '好'],
        ['老年', '是', '否', '非常好'],
        ['老年', '否', '否', '一般'],
    ])
    testY = np.array(['否', '否', '是', '是', '否', '否', '否', '是', '是', '是', '是', '是', '是', '是', '否'])

    # show in table
    pred = cart.predict(testX)
    table = Table('x', 'y', 'pred')
    for x, y, y_hat in zip(testX, testY, pred):
        table.add_row(*map(str, [x, y, y_hat]))
    console.print(table)
