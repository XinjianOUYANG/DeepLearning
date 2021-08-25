# Adaboost & GBDT

## 集成学习(Ensemble Learning）

[集成学习](https://blog.csdn.net/Daycym/article/details/81909690)就是通过构建并结合多个学习器来完成学习任务。 然后根据个体学习器的生成方式，介绍了集成学习方法两大类：

* 个体学习器间存在强依赖关系，必须串行生成的序列化方法，代表是：Boosting
* 个体学习器间不存在强依赖关系，可同时生成的并列化方法，代表是：Bagging和随机森林（Random Forest）

## Adaboost 算法步骤

[参考博客](https://blog.csdn.net/Daycym/article/details/81915699)

提升（Boosting）方法是一种常用的统计学习方法，应用广泛且有效。在分类问题中，它通过改变训练样本的权重，学习多个分类器，并将这些分类器进行线性组合，提高分类的性能。

对于提升方法来说，有两个问题需要回答：

* 在每一轮如何改变训练数据的权重或概率分布
* 如何将弱分类器组合成一个强分类器

AdaBoostAdaBoost的做法是，提高那些被前一轮弱分类器错误分类样本的权值，而降低那些被正确分类样本的权值。这样一来，在那些没有得到正确分类的数据，由于其权值的加大而受到后一轮的弱分类器的更大关注，于是，分类问题被一系列的弱分类器“分而治之”。

至于第二个问题，AdaBoostAdaBoost采取加权多数表决的方法。具体地，加大分类误差率小的弱分类器的权值，使其在表决中起较大的作用，减小分类误差率大的弱分类器的权值，使其在表决中起较小的作用。

## 梯度提升决策树（Gradient Boosting Decision Tree, GDBT)

* `[A Gentle Introduction to the Gradient Boosting Algorithm for Machine Learning](https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/)
* GBDT采用了多模型集成的策略，针对残差进行拟合，进而降低模型的偏差和方差.
* 我们评价一个模型的预测能力，一般考察残差的两个方面：（1）偏差，即与真实值分布的偏差大小；（2）方差，体现模型预测能力的稳定性，或者说鲁棒性。

### GBDT 改进

（1） 在预测阶段，每个CART是独立的，因此可以并行计算。另外，得益于决策树的高效率，GBDT在预测阶段的计算速度是非常快的。

（2） 在训练阶段，GBDT里的CART之间存在依赖，无法并行，所以GBDT的训练速度是比较慢的。人们提出了一些方法，用来提升这个阶段的并行度，以提升学习速度。

（3） 这里为了简单，使用了残差平方和作为损失函数，实际上还可以使用绝对值损失函数、huber损失函数等，从而让GBDT在鲁棒性等方面得到提升。

（4） GBDT的学习能力非常强，容易过拟合。大部分时候，我们都会给目标函数添加针对模型复杂度的惩罚项，从而控制模型复杂度

[GBDT(梯度提升决策树)——来由、原理和python实现](https://zhuanlan.zhihu.com/p/144855223)
