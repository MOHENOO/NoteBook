# Google机器学习

## 前提条件和准备工作

### Pandas使用入门

### 低阶TensorFlow基础知识

### 主要概念和工具

### Python编程

什么是（监督式）机器学习？简单来说，它的定义如下：

机器学习系统通过学习如何组合输入信息来对从未见过的数据做出有用的预测。
下面我们来了解一下机器学习的基本术语。

标签
标签是我们要预测的事物，即简单线性回归中的 y 变量。标签可以是小麦未来的价格、图片中显示的动物品种、音频剪辑的含义或任何事物。

特征
特征是输入变量，即简单线性回归中的 x 变量。简单的机器学习项目可能会使用单个特征，而比较复杂的机器学习项目可能会使用数百万个特征，按如下方式指定：

在垃圾邮件检测器示例中，特征可能包括：

电子邮件文本中的字词
发件人的地址
发送电子邮件的时段
电子邮件中包含“一种奇怪的把戏”这样的短语。
样本
样本是指数据的特定实例：x。（我们采用粗体 x 表示它是一个矢量。）我们将样本分为以下两类：

有标签样本
无标签样本
有标签样本同时包含特征和标签。即：

  labeled examples: {features, label}: (x, y)
我们使用有标签样本来训练模型。在我们的垃圾邮件检测器示例中，有标签样本是用户明确标记为“垃圾邮件”或“非垃圾邮件”的各个电子邮件。

例如，下表显示了从包含加利福尼亚州房价信息的数据集中抽取的 5 个有标签样本：

housingMedianAge
（特征）	totalRooms
（特征）	totalBedrooms
（特征）	medianHouseValue
（标签）
15	5612	1283	66900
19	7650	1901	80100
17	720	174	85700
14	1501	337	73400
20	1454	326	65500
无标签样本包含特征，但不包含标签。即：

  unlabeled examples: {features, ?}: (x, ?)
以下是取自同一住房数据集的 3 个无标签样本，其中不包含 medianHouseValue：

housingMedianAge
（特征）	totalRooms
（特征）	totalBedrooms
（特征）
42	1686	361
34	1226	180
33	1077	271
在使用有标签样本训练模型之后，我们会使用该模型预测无标签样本的标签。在垃圾邮件检测器示例中，无标签样本是用户尚未添加标签的新电子邮件。

模型
模型定义了特征与标签之间的关系。例如，垃圾邮件检测模型可能会将某些特征与“垃圾邮件”紧密联系起来。我们来重点介绍一下模型生命周期的两个阶段：

训练是指创建或学习模型。也就是说，向模型展示有标签样本，让模型逐渐学习特征与标签之间的关系。

推断是指将训练后的模型应用于无标签样本。也就是说，使用经过训练的模型做出有用的预测 (y')。例如，在推断期间，您可以针对新的无标签样本预测 medianHouseValue。

回归与分类
回归模型可预测连续值。例如，回归模型做出的预测可回答如下问题：

加利福尼亚州一栋房产的价值是多少？

用户点击此广告的概率是多少？

分类模型可预测离散值。例如，分类模型做出的预测可回答如下问题：

某个指定电子邮件是垃圾邮件还是非垃圾邮件？

这是一张狗、猫还是仓鼠图片？

## TensorFlow

TensorFlow 的名称源自张量，张量是任意维度的数组。借助 TensorFlow，您可以操控具有大量维度的张量。即便如此，在大多数情况下，您会使用以下一个或多个低维张量：

标量是零维数组（零阶张量）。例如，\'Howdy\' 或 5
矢量是一维数组（一阶张量）。例如，[2, 3, 5, 7, 11] 或 [5]
矩阵是二维数组（二阶张量）。例如，[[3.1, 8.2, 5.9][4.3, -2.7, 6.5]]
TensorFlow 指令会创建、销毁和操控张量。典型 TensorFlow 程序中的大多数代码行都是指令。

TensorFlow 图（也称为计算图或数据流图）是一种图数据结构。很多 TensorFlow 程序由单个图构成，但是 TensorFlow 程序可以选择创建多个图。图的节点是指令；图的边是张量。张量流经图，在每个节点由一个指令操控。一个指令的输出张量通常会变成后续指令的输入张量。TensorFlow 会实现延迟执行模型，意味着系统仅会根据相关节点的需求在需要时计算节点。

张量可以作为常量或变量存储在图中。您可能已经猜到，常量存储的是值不会发生更改的张量，而变量存储的是值会发生更改的张量。不过，您可能没有猜到的是，常量和变量都只是图中的一种指令。常量是始终会返回同一张量值的指令。变量是会返回分配给它的任何张量的指令。

要定义常量，请使用 tf.constant 指令，并传入它的值。例如：

```python
x = tf.constant([5.2])
```

同样，您可以创建如下变量：

```python
  y = tf.Variable([5])
```

或者，您也可以先创建变量，然后再如下所示地分配一个值（注意：您始终需要指定一个默认值）：

```python
  y = tf.Variable([0])
  y = y.assign([5])
```

定义一些常量或变量后，您可以将它们与其他指令（如 tf.add）结合使用。在评估 tf.add 指令时，它会调用您的 tf.constant 或 tf.Variable 指令，以获取它们的值，然后返回一个包含这些值之和的新张量。

图必须在 TensorFlow 会话中运行，会话存储了它所运行的图的状态：

将 tf.Session() 作为会话：

```python
  initialization = tf.global_variables_initializer()
  print(y.eval())
```

在使用 tf.Variable 时，您必须在会话开始时调用 tf.global_variables_initializer，以明确初始化这些变量，如上所示。

注意：会话可以将图分发到多个机器上执行（假设程序在某个分布式计算框架上运行）。有关详情，请参阅分布式 TensorFlow。

总结
TensorFlow 编程本质上是一个两步流程：

将常量、变量和指令整合到一个图中。
在一个会话中评估这些常量、变量和指令。
创建一个简单的 TensorFlow 程序
我们来看看如何编写一个将两个常量相加的简单 TensorFlow 程序。

添加 import 语句
与几乎所有 Python 程序一样，您首先要添加一些 import 语句。 当然，运行 TensorFlow 程序所需的 import 语句组合取决于您的程序将要访问的功能。至少，您必须在所有 TensorFlow 程序中添加 import tensorflow 语句：
import tensorflow as tf
请勿忘记执行前面的代码块（import 语句）。

其他常见的 import 语句包括：

import matplotlib.pyplot as plt # 数据集可视化。
import numpy as np              # 低级数字 Python 库。
import pandas as pd             # 较高级别的数字 Python 库。
TensorFlow 提供了一个默认图。不过，我们建议您明确创建自己的 Graph，以便跟踪状态（例如，您可能希望在每个单元格中使用一个不同的 Graph）。

```python
from __future__ import print_function

import tensorflow as tf

# Create a graph.
g = tf.Graph()

# Establish the graph as the "default" graph.
with g.as_default():
  # Assemble a graph consisting of the following three operations:
  #   * Two tf.constant operations to create the operands.
  #   * One tf.add operation to add the two operands.
  x = tf.constant(8, name="x_const")
  y = tf.constant(5, name="y_const")
  sum = tf.add(x, y, name="x_y_sum")


  # Now create a session.
  # The session will run the default graph.
  with tf.Session() as sess:
    print(sum.eval())
from __future__ import print_function
​
import tensorflow as tf
​
# Create a graph.
g = tf.Graph()
​
# Establish the graph as the "default" graph.
with g.as_default():
  # Assemble a graph consisting of the following three operations:
  #   * Two tf.constant operations to create the operands.
  #   * One tf.add operation to add the two operands.
  x = tf.constant(8, name="x_const")
  y = tf.constant(5, name="y_const")
  sum = tf.add(x, y, name="x_y_sum")
​
​
  # Now create a session.
  # The session will run the default graph.
  with tf.Session() as sess:
    print(sum.eval())
```