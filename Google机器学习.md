# Google机器学习

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

## 使用TensorFlow的基本步骤

```python
# %%
from __future__ import print_function
import math

from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

# 设置
tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

# 导入加利福尼亚州房屋数据
california_housing_dataframe = pd.read_csv(
    "https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv", sep=",")

# 随机重排
california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"] /= 1000.0

california_housing_dataframe.describe()

# 第 1 步：定义特征并配置特征列
# Define the input feature: total_rooms.
# 数据输入特征房间总数
my_feature = california_housing_dataframe[["total_rooms"]]
# Configure a numeric feature column for total_rooms.
# 使用numeric_column定义特征列
feature_columns = [tf.feature_column.numeric_column("total_rooms")]

# 第 2 步：定义目标
# Define the label.
targets = california_housing_dataframe["median_house_value"]

# 第 3 步：配置 LinearRegressor(线性回归模型)
# Use gradient descent as the optimizer for training the model.
# 使用 GradientDescentOptimizer（它会实现小批量随机梯度下降法 (SGD)）训练该模型。learning_rate 参数可控制梯度步长的大小。
my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0000001)
# 注意：为了安全起见，我们还会通过 clip_gradients_by_norm 将梯度裁剪应用到我们的优化器。梯度裁剪可确保梯度大小在训练期间不会变得过大，梯度过大会导致梯度下降法失败。
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

# Configure the linear regression model with our feature columns and optimizer.
# Set a learing rate of 0.0000001 for Gradient Descent.
linear_regressor = tf.estimator.LinearRegressor(
    feature_columns=feature_columns, optimizer=my_optimizer)


# 第 4 步：定义输入函数
# 要将加利福尼亚州住房数据导入 LinearRegressor，我们需要定义一个输入函数，让它告诉 TensorFlow 如何对数据进行预处理，以及在模型训练期间如何批处理、随机处理和重复数据。

# 首先，我们将 Pandas 特征数据转换成 NumPy 数组字典。然后，我们可以使用 TensorFlow Dataset API 根据我们的数据构建 Dataset 对象，并将数据拆分成大小为 batch_size 的多批数据，以按照指定周期数 (num_epochs) 进行重复。
# 注意：如果将默认值 num_epochs=None 传递到 repeat()，输入数据会无限期重复。
# 然后，如果 shuffle 设置为 True，则我们会对数据进行随机处理，以便数据在训练期间以随机方式传递到模型。buffer_size 参数会指定 shuffle 将从中随机抽样的数据集的大小。
# 最后，输入函数会为该数据集构建一个迭代器，并向 LinearRegressor 返回下一批数据。
def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    """Trains a linear regression model of one feature.
    Args:
        features: pandas DataFrame of features
      targets: pandas DataFrame of targets
      batch_size: Size of batches to be passed to the model
      shuffle: True or False. Whether to shuffle the data.
      num_epochs: Number of epochs for which data should be repeated. None = repeat indefinitely
    Returns:
      Tuple of (features, labels) for next data batch
    """

    # Convert pandas data into a dict of np arrays.
    features = {key: np.array(value) for key, value in dict(features).items()}

    # Construct a dataset,and configure batching/repeating.
    ds = Dataset.from_tensor_slices((features, targets))  # warning:2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)

    # Shuffle the data, if specified.
    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    # Return the next batch of data.
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels


# 第 5 步：训练模型
_ = linear_regressor.train(
    input_fn=lambda: my_input_fn(my_feature, targets), steps=100)

# 第 6 步：评估模型
# 我们基于该训练数据做一次预测，看看我们的模型在训练期间与这些数据的拟合情况。
# 注意：训练误差可以衡量您的模型与训练数据的拟合情况，但并_不能_衡量模型泛化到新数据的效果。在后面的练习中，您将探索如何拆分数据以评估模型的泛化能力。

# Create an input function for predictions.
# Note: Since we're making just one prediction for each example, we don't
# need to repeat or shuffle the data here.


def prediction_input_fn(): return my_input_fn(
    my_feature, targets, num_epochs=1, shuffle=False)


# Call predict() on the linear_regressor to make predictions.
predictions = linear_regressor.predict(input_fn=prediction_input_fn)

# Format predictions as a NumPy array, so we can calculate error metrics.
predictions = np.array([item['predictions'][0] for item in predictions])

# Print Mean Squared Error and Root Mean Squared Error.
mean_squared_error = metrics.mean_squared_error(predictions, targets)
root_mean_squared_error = math.sqrt(mean_squared_error)
print("Mean Squared Error (on training data): %0.3f" % mean_squared_error)
print("Root Mean Squared Error (on training data): %0.3f" %
      root_mean_squared_error)

# 这是出色的模型吗？您如何判断误差有多大？
# 由于均方误差 (MSE) 很难解读，因此我们经常查看的是均方根误差 (RMSE)。RMSE 的一个很好的特性是，它可以在与原目标相同的规模下解读。
# 我们来比较一下 RMSE 与目标最大值和最小值的差值：

min_house_value = california_housing_dataframe["median_house_value"].min()
max_house_value = california_housing_dataframe["median_house_value"].max()
min_max_difference = max_house_value - min_house_value

print("Min. Median House Value: %0.3f" % min_house_value)
print("Max. Median House Value: %0.3f" % max_house_value)
print("Difference between Min. and Max.: %0.3f" % min_max_difference)
print("Root Mean Squared Error: %0.3f" % root_mean_squared_error)

#from __future__ import print_function


# 设置
tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

# 导入加利福尼亚州房屋数据
california_housing_dataframe = pd.read_csv(
    "https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv", sep=",")

# 随机重排
california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"] /= 1000.0

california_housing_dataframe.describe()

# 第 1 步：定义特征并配置特征列
# Define the input feature: total_rooms.
# 数据输入特征房间总数
my_feature = california_housing_dataframe[["total_rooms"]]
# Configure a numeric feature column for total_rooms.
# 使用numeric_column定义特征列
feature_columns = [tf.feature_column.numeric_column("total_rooms")]

# 第 2 步：定义目标
# Define the label.
targets = california_housing_dataframe["median_house_value"]

# 第 3 步：配置 LinearRegressor(线性回归模型)
# Use gradient descent as the optimizer for training the model.
# 使用 GradientDescentOptimizer（它会实现小批量随机梯度下降法 (SGD)）训练该模型。learning_rate 参数可控制梯度步长的大小。
my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0000001)
# 注意：为了安全起见，我们还会通过 clip_gradients_by_norm 将梯度裁剪应用到我们的优化器。梯度裁剪可确保梯度大小在训练期间不会变得过大，梯度过大会导致梯度下降法失败。
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

# Configure the linear regression model with our feature columns and optimizer.
# Set a learing rate of 0.0000001 for Gradient Descent.
linear_regressor = tf.estimator.LinearRegressor(
    feature_columns=feature_columns, optimizer=my_optimizer)


# 第 4 步：定义输入函数
# 要将加利福尼亚州住房数据导入 LinearRegressor，我们需要定义一个输入函数，让它告诉 TensorFlow 如何对数据进行预处理，以及在模型训练期间如何批处理、随机处理和重复数据。

# 首先，我们将 Pandas 特征数据转换成 NumPy 数组字典。然后，我们可以使用 TensorFlow Dataset API 根据我们的数据构建 Dataset 对象，并将数据拆分成大小为 batch_size 的多批数据，以按照指定周期数 (num_epochs) 进行重复。
# 注意：如果将默认值 num_epochs=None 传递到 repeat()，输入数据会无限期重复。
# 然后，如果 shuffle 设置为 True，则我们会对数据进行随机处理，以便数据在训练期间以随机方式传递到模型。buffer_size 参数会指定 shuffle 将从中随机抽样的数据集的大小。
# 最后，输入函数会为该数据集构建一个迭代器，并向 LinearRegressor 返回下一批数据。
def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    """Trains a linear regression model of one feature.
    Args:
        features: pandas DataFrame of features
      targets: pandas DataFrame of targets
      batch_size: Size of batches to be passed to the model
      shuffle: True or False. Whether to shuffle the data.
      num_epochs: Number of epochs for which data should be repeated. None = repeat indefinitely
    Returns:
      Tuple of (features, labels) for next data batch
    """

    # Convert pandas data into a dict of np arrays.
    features = {key: np.array(value) for key, value in dict(features).items()}

    # Construct a dataset,and configure batching/repeating.
    ds = Dataset.from_tensor_slices((features, targets))  # warning:2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)

    # Shuffle the data, if specified.
    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    # Return the next batch of data.
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels


# 第 5 步：训练模型
_ = linear_regressor.train(
    input_fn=lambda: my_input_fn(my_feature, targets), steps=100)

# 第 6 步：评估模型
# 我们基于该训练数据做一次预测，看看我们的模型在训练期间与这些数据的拟合情况。
# 注意：训练误差可以衡量您的模型与训练数据的拟合情况，但并_不能_衡量模型泛化到新数据的效果。在后面的练习中，您将探索如何拆分数据以评估模型的泛化能力。

# Create an input function for predictions.
# Note: Since we're making just one prediction for each example, we don't
# need to repeat or shuffle the data here.


def prediction_input_fn(): return my_input_fn(
    my_feature, targets, num_epochs=1, shuffle=False)


# Call predict() on the linear_regressor to make predictions.
predictions = linear_regressor.predict(input_fn=prediction_input_fn)

# Format predictions as a NumPy array, so we can calculate error metrics.
predictions = np.array([item['predictions'][0] for item in predictions])

# Print Mean Squared Error and Root Mean Squared Error.
mean_squared_error = metrics.mean_squared_error(predictions, targets)
root_mean_squared_error = math.sqrt(mean_squared_error)
print("Mean Squared Error (on training data): %0.3f" % mean_squared_error)
print("Root Mean Squared Error (on training data): %0.3f" %
      root_mean_squared_error)

# 这是出色的模型吗？您如何判断误差有多大？
# 由于均方误差 (MSE) 很难解读，因此我们经常查看的是均方根误差 (RMSE)。RMSE 的一个很好的特性是，它可以在与原目标相同的规模下解读。
# 我们来比较一下 RMSE 与目标最大值和最小值的差值：

min_house_value = california_housing_dataframe["median_house_value"].min()
max_house_value = california_housing_dataframe["median_house_value"].max()
min_max_difference = max_house_value - min_house_value

print("Min. Median House Value: %0.3f" % min_house_value)
print("Max. Median House Value: %0.3f" % max_house_value)
print("Difference between Min. and Max.: %0.3f" % min_max_difference)
print("Root Mean Squared Error: %0.3f" % root_mean_squared_error)
# Mean Squared Error (on training data): 56367.025
# Root Mean Squared Error (on training data): 237.417
# Min. Median House Value: 14.999
# Max. Median House Value: 500.001
# Difference between Min. and Max.: 485.002
# Root Mean Squared Error: 237.417
# 我们的误差跨越目标值的近一半范围，可以进一步缩小误差吗？
# 这是每个模型开发者都会烦恼的问题。我们来制定一些基本策略，以降低模型误差。
# 首先，我们可以了解一下根据总体摘要统计信息，预测和目标的符合情况。
calibration_data = pd.DataFrame()
calibration_data["predictions"] = pd.Series(predictions)
calibration_data["targets"] = pd.Series(targets)
calibration_data.describe()

# 好的，此信息也许有帮助。平均值与模型的 RMSE 相比情况如何？各种分位数呢？
# 我们还可以将数据和学到的线可视化。我们已经知道，单个特征的线性回归可绘制成一条将输入 x 映射到输出 y 的线。
# 首先，我们将获得均匀分布的随机数据样本，以便绘制可辨的散点图。
sample = california_housing_dataframe.sample(n=300)

# 然后，我们根据模型的偏差项和特征权重绘制学到的线，并绘制散点图。该线会以红色显示。
# Get the min and max total_rooms values.
x_0 = sample["total_rooms"].min()
x_1 = sample["total_rooms"].max()

# Retrieve the final weight and bias generated during training.
weight = linear_regressor.get_variable_value(
    'linear/linear_model/total_rooms/weights')[0]
bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')

# Get the predicted median_house_values for the min and max total_rooms values.
y_0 = weight * x_0 + bias
y_1 = weight * x_1 + bias

# Plot our regression line from (x_0, y_0) to (x_1, y_1).
plt.plot([x_0, x_1], [y_0, y_1], c='r')

# Label the graph axes.
plt.ylabel("median_house_value")
plt.xlabel("total_rooms")

# Plot a scatter plot from our data sample.
plt.scatter(sample["total_rooms"], sample["median_house_value"])

# Display graph.
plt.show()
# 这条初始线看起来与目标相差很大。看看您能否回想起摘要统计信息，并看到其中蕴含的相同信息。
# 综上所述，这些初始健全性检查提示我们也许可以找到更好的线。


# 调整模型超参数
# 对于本练习，为方便起见，我们已将上述所有代码放入一个函数中。您可以使用不同的参数调用该函数，以了解相应效果。
# 我们会在 10 个等分的时间段内使用此函数，以便观察模型在每个时间段的改善情况。
# 对于每个时间段，我们都会计算训练损失并绘制相应图表。这可以帮助您判断模型收敛的时间，或者模型是否需要更多迭代。
# 此外，我们还会绘制模型随着时间的推移学习的特征权重和偏差项值的曲线图。您还可以通过这种方式查看模型的收敛效果。


def train_model(learning_rate, steps, batch_size, input_feature="total_rooms"):
    """Trains a linear regression model of one feature.

    Args:
      learning_rate: A `float`, the learning rate.
      steps: A non-zero `int`, the total number of training steps. A training step
        consists of a forward and backward pass using a single batch.
      batch_size: A non-zero `int`, the batch size.
      input_feature: A `string` specifying a column from `california_housing_dataframe`
        to use as input feature.
    """

    periods = 10
    steps_per_period = steps / periods

    my_feature = input_feature
    my_feature_data = california_housing_dataframe[[my_feature]]
    my_label = "median_house_value"
    targets = california_housing_dataframe[my_label]

    # Create feature columns.
    feature_columns = [tf.feature_column.numeric_column(my_feature)]

    # Create input functions.
    def training_input_fn(): return my_input_fn(
        my_feature_data, targets, batch_size=batch_size)

    def prediction_input_fn(): return my_input_fn(
        my_feature_data, targets, num_epochs=1, shuffle=False)

    # Create a linear regressor object.
    my_optimizer = tf.train.GradientDescentOptimizer(
        learning_rate=learning_rate)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(
        my_optimizer, 5.0)
    linear_regressor = tf.estimator.LinearRegressor(
        feature_columns=feature_columns,
        optimizer=my_optimizer
    )

    # Set up to plot the state of our model's line each period.
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    plt.title("Learned Line by Period")
    plt.ylabel(my_label)
    plt.xlabel(my_feature)
    sample = california_housing_dataframe.sample(n=300)
    plt.scatter(sample[my_feature], sample[my_label])
    colors = [cm.coolwarm(x) for x in np.linspace(-1, 1, periods)]

    # Train the model, but do so inside a loop so that we can periodically assess
    # loss metrics.
    print("Training model...")
    print("RMSE (on training data):")
    root_mean_squared_errors = []
    for period in range(0, periods):
        # Train the model, starting from the prior state.
        linear_regressor.train(
            input_fn=training_input_fn,
            steps=steps_per_period
        )
        # Take a break and compute predictions.
        predictions = linear_regressor.predict(input_fn=prediction_input_fn)
        predictions = np.array([item['predictions'][0]
                                for item in predictions])

        # Compute loss.
        root_mean_squared_error = math.sqrt(
            metrics.mean_squared_error(predictions, targets))
        # Occasionally print the current loss.
        print("  period %02d : %0.2f" % (period, root_mean_squared_error))
        # Add the loss metrics from this period to our list.
        root_mean_squared_errors.append(root_mean_squared_error)
        # Finally, track the weights and biases over time.
        # Apply some math to ensure that the data and line are plotted neatly.
        y_extents = np.array([0, sample[my_label].max()])

        weight = linear_regressor.get_variable_value(
            'linear/linear_model/%s/weights' % input_feature)[0]
        bias = linear_regressor.get_variable_value(
            'linear/linear_model/bias_weights')

        x_extents = (y_extents - bias) / weight
        x_extents = np.maximum(np.minimum(x_extents,
                                          sample[my_feature].max()),
                               sample[my_feature].min())
        y_extents = weight * x_extents + bias
        plt.plot(x_extents, y_extents, color=colors[period])
    print("Model training finished.")

    # Output a graph of loss metrics over periods.
    plt.subplot(1, 2, 2)
    plt.ylabel('RMSE')
    plt.xlabel('Periods')
    plt.title("Root Mean Squared Error vs. Periods")
    plt.tight_layout()
    plt.plot(root_mean_squared_errors)

    # Output a table with calibration data.
    calibration_data = pd.DataFrame()
    calibration_data["predictions"] = pd.Series(predictions)
    calibration_data["targets"] = pd.Series(targets)
    display.display(calibration_data.describe())

    print("Final RMSE (on training data): %0.2f" % root_mean_squared_error)


# train_model(
#     learning_rate=0.00002,
#     steps=500,
#     batch_size=5
# )

train_model(
    learning_rate=0.00002,
    steps=1000,
    batch_size=5,
    input_feature="population"
)
```

## 合成特征和离群值

```python

```