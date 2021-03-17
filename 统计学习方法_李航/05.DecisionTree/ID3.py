from pprint import pprint # Pretty-print a Python object to a stream [default is sys.stdout].
from rich.console import Console
from rich.table import Table
from collections import Counter
import sys
import os
from pathlib import Path
sys.path.append(str(Path(os.path.abspath(__file__)).parent.parent))
from utils import argmax, information_gain

# 在决策树的各个节点上应用信息增益准则选择特征，递归地构建决策树
# 用极大似然法进行概率模型的选择
# ID3算法只有树的生成（无剪枝），容易过拟合
class ID3:
    class Node:
        def __init__(self, col, Y):
            self.col = col # 特征/属性
            self.children = {}
            self.prob = Counter(Y)
            s = sum(self.prob.values())
            for y in self.prob:
                self.prob[y] /= s   # 归一化， normalisation
            label_ind, self.label_prob = argmax(self.prob.keys(),
                                                key=self.prob.__getitem__)
            self.label = Y[label_ind] # label = y,决策

    def __init__(self, information_gain_threshold=0., verbose=False):
        self.information_gain_threshold = information_gain_threshold
        self.verbose = verbose

    def fit(self, X, Y):
        self.column_cnt = len(X[0]) # 特征数量
        self.root = self.build(X, Y, set())

    def build(self, X, Y, selected):
        #print('counter(T)',Counter(Y))
        cur = self.Node(None, Y) # current node
        if self.verbose:
            print("Cur selected columns(including previous selected cols):", selected)
            print("Cur data:")
            pprint(X)
            print(Y)
        split = False
        # check if there is no attribute to choose
        # or there is no need for spilt
        if len(selected) != self.column_cnt and len(set(Y)) > 1:
            
            print(list(set(range(self.column_cnt))),'selected feature:',selected,'\n') 

            left_columns = list(set(range(self.column_cnt)) - selected)
            # 遍历col， 选择信息增益最大的col/特征, 返回特征数字指标和最大信息增益
            col_ind, best_information_gain = argmax(left_columns,
                                                    key=lambda col: information_gain(X, Y, col))
            '''
            def argmax(arr, key=lambda x: x):
                arr = [key(a) for a in arr]
                ans = max(arr)
                return arr.index(ans), ans
            '''
            col = left_columns[col_ind]
            # if this split is better than not splitting
            if best_information_gain >= self.information_gain_threshold:
                print(f"Split by {col}th column")
                split = True
                cur.col = col
                for val in set(x[col] for x in X):
                    # 递归
                    ind = [val == x[col] for x in X]
                    # print('ind',ind)
                    child_X = [x for i, x in zip(ind, X) if i]
                    child_Y = [y for i, y in zip(ind, Y) if i]
                    cur.children[val] = self.build(child_X, child_Y, selected | {col})  # selected | {col} 并集
        if not split:
            print("No split")
        return cur

    def query(self, root, x):
        if root.col is None or x[root.col] not in root.children:
            return root.label
        return self.query(root.children[x[root.col]], x)

    def _predict(self, x):
        return self.query(self.root, x)

    def predict(self, X):
        return [self._predict(x) for x in X]


if __name__ == "__main__":
    console = Console(markup=False)
    id3 = ID3(verbose=True)
    # -------------------------- Example 1 ----------------------------------------
    # unpruned decision tree predict correctly for all training data
    print("Example 1:")
    X = [
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
    ]
    Y = ['否', '否', '是', '是', '否', '否', '否', '是', '是', '是', '是', '是', '是', '是', '否']
    # print('set(Y):',set(Y),'\n')
    id3.fit(X, Y)

    # show in table
    pred = id3.predict(X)
    table = Table('x', 'y', 'pred')
    for x, y, y_hat in zip(X, Y, pred):
        table.add_row(*map(str, [x, y, y_hat]))
    console.print(table)

    # # -------------------------- Example 2 ----------------------------------------
    # # but unpruned（修剪） decision tree doesn't generalize well for test data
    # print("Example 2:")
    # X = [
    #     ['青年', '否', '否', '一般'],
    #     ['青年', '否', '否', '好'],
    #     ['青年', '是', '是', '一般'],
    #     ['青年', '否', '否', '一般'],
    #     ['老年', '否', '否', '一般'],
    #     ['老年', '否', '否', '好'],
    #     ['老年', '是', '是', '好'],
    #     ['老年', '否', '是', '非常好'],
    #     ['老年', '否', '是', '非常好'],
    #     ['老年', '否', '是', '非常好'],
    #     ['老年', '否', '是', '好'],
    #     ['老年', '否', '否', '一般'],
    # ]
    # Y = ['否', '否', '是', '否', '否', '否', '是', '是', '是', '是', '是', '否']
    # id3.fit(X, Y)

    # testX = [
    #     ['青年', '否', '否', '一般'],
    #     ['青年', '否', '否', '好'],
    #     ['青年', '是', '否', '好'],
    #     ['青年', '是', '是', '一般'],
    #     ['青年', '否', '否', '一般'],
    #     ['老年', '否', '否', '一般'],
    #     ['老年', '否', '否', '好'],
    #     ['老年', '是', '是', '好'],
    #     ['老年', '否', '是', '非常好'],
    #     ['老年', '否', '是', '非常好'],
    #     ['老年', '否', '是', '非常好'],
    #     ['老年', '否', '是', '好'],
    #     ['老年', '是', '否', '好'],
    #     ['老年', '是', '否', '非常好'],
    #     ['老年', '否', '否', '一般'],
    # ]
    # testY = ['否', '否', '是', '是', '否', '否', '否', '是', '是', '是', '是', '是', '是', '是', '否']

    # # show in table
    # pred = id3.predict(testX)
    # table = Table('x', 'y', 'pred')
    # for x, y, y_hat in zip(testX, testY, pred):
    #     table.add_row(*map(str, [x, y, y_hat]))
    # console.print(table)
