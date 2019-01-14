# 利用python进行数据分析

## 引言

2011年，URL缩短服务bit.ly跟美国政府网站usa.gov合作，提供了一份从生成.gov或.mil短链接的拥挤那里收集的匿名数据。

时区统计(数据来自bit.ly的1.usa.gov)

```python
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
from pandas import DataFrame, Series
import numpy as np
import pandas as pd
from collections import Counter
from collections import defaultdict

# %%
# bit.ly的匿名数据
import json
path = "usagov_bitly_data2013-05-17-1368832207.txt"
records = [json.loads(line) for line in open(path)]
records[0]

# %%
records[0]["tz"]

# %%
# 不是所有记录都有时区字段
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]

# %%
# 对时区进行计数


def get_count(sequence):
    counts = defaultdict(int)  # 初始化所有值为0
    for x in sequence:
        counts[x] += 1
    return counts


counts = get_count(time_zones)
counts['America/New_York']

# %%
len(time_zones)

# %%


def top_counts(count_dict, n=10):
    """
    return a sorted list[n:] of dict
    """
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:][::-1]


top_counts(counts)

# %%
# 使用 collections.Counter 计数时区

counts = Counter(time_zones)
counts.most_common(10)


# %%
# 使用pandas 时区计数
frame = DataFrame(records)
frame

tz_counts = frame['tz'].value_counts()
tz_counts[:10]
clean_tz = frame['tz'].fillna("Missing")
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10]
tz_counts[:10].plot(kind='barh', rot=0)

# %%
frame['a'][1]


# %%
# 分离agent信息
results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
# %%
results.value_counts()[:8]


# %%
# 区分windows和非windows
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe["a"].str.contains(
    "Windows"), "Windows", "Not Windows")

# %%
# 根据时区和操作系统列表对数据分组
by_tz_os = cframe.groupby(['tz', operating_system])

# %%
# 通过size对分组结果进行计数，利用unstack对计数结果进行重塑
agg_counts = by_tz_os.size().unstack().fillna(0)
agg_counts[:10]

# %%
# 选取最常出现的时区，根据agg_counts中的行数构造一个间接索引数组
# 用于升序排列
indexer = agg_counts.sum(1).argsort()
indexer[:10]

# %%
# 通过take截取最后10行
count_subset = agg_counts.take(indexer)[-10:]
count_subset

# %%
# 通过stacked=True，生成一张堆积条形图
count_subset.plot(kind='barh', stacked=True)

# %%
# 各行规范化为“总计为1”
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
```

## Numpy

### Numpy的ndarray：一种多维数组对象

NumPy最重要的一个特点就是其N维数组对象，该对象是一个快速而灵活的大数据集容器。你可以利用这种数组对整块数据执行一些数学运算，其语法跟标量元素之间的运算一样。

ndarray是一个通用的同构数据多维容器，也就是说，其中的所有元素必须是相同类型的。每个数组都有一个shape（一个表示各维度大小的元组）和一个dtype（一个用于说明数组数据类型的对象）。

### 创建ndarray

创建数组最简单的办法是使用array函数。它接受一切序列型的对象（包括其他数组），然后产生一个新的含有传入数据的NumPy数组。以一个列表的转换为例：

```python
# %%
import numpy as np
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
arr1
#array([6. , 7.5, 8. , 0. , 1. ])

# %%
#嵌套序列（比如由一组等长度列表组成的列表）将会转换为一个多维数组
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2
# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])

# %%
arr2.ndim
#2
# %%
arr2.shape
# (2,4)
# %%
#除非显示说明，np.array会尝试为新建的这个数组推断出一个较为合适的数据类型。数据类型保存在一个特殊的dtype对象中
arr1.dtype

arr1.dtype
# dtype('float64')
# %%
arr2.dtype
# dtype('int64')
```

除np.array之外，还有一些函数也可以新建数组。比如，zeros和ones分别可以创建指定长度或形状的全0或全1数组。empty可以创建一个没有任何具体值的数组。

```python
# %%
np.zeros(10)
#array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
# %%
np.zeros((3, 6))
# array([[0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0.]])
# %%
#np.empty返回的是一些未初始化的垃圾值
np.empty((2, 3, 2))
# array([[[2.41907520e-312, 2.14321575e-312],
#         [2.46151512e-312, 2.31297541e-312],
#         [2.35541533e-312, 2.05833592e-312]],

#        [[2.22809558e-312, 2.56761491e-312],
#         [2.48273508e-312, 2.05833592e-312],
#         [2.05833592e-312, 2.29175545e-312]]])
# %%
#arange是Python内置函数range的数组版
np.arange(15)
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
```

### ndrray的数据类型

dtype（数据类型）是一个特殊的对象，它含有ndarray将一块内存解释为特定数据类型所需的信息。

```python
arr1=np.array([1,2,3],dtype=np.float64)
```

dtype是NumPy如此强大和灵活的原因之一。多数情况下，它们直接映射到相应的机器表示，这使得“读写磁盘上的二进制数据流”以及“集成低级语言代码（如C，Forrtan”等工作变得更加容易。

你可以通过ndarray的astype方法显示地转换其dtype

如果转换浮点数成整数，则小数部分会被截断

```python
arr = np.array([3.7, 1.2, -2.5])

arr.astype(np.int32)
arr = np.array([3.7, 1.2, -2.5])

arr.astype(np.int32)
# array([ 3,  1, -2], dtype=int32)
```

如果转换过程因为某种原因而失败了，就会引发一个TypeError。

调用astype无论如何都会创建出一个新的数组（原始数据的一份拷贝），即使新dtype跟老dtype相同也是如此。

### 数组和标量之间的运算

数组很重要，因为它使你不用编写循环即可对数据进行批量运算。这通常叫做矢量化。大小相等的数组之间的任何算术运算都会运算应用到元素级：

```python
# %%
import numpy as np
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr
# array([[1., 2., 3.],
#        [4., 5., 6.]])

# %%
arr * arr

arr * arr
# array([[ 1.,  4.,  9.],
#        [16., 25., 36.]])
# %%
arr - arr
# array([[0., 0., 0.],
#        [0., 0., 0.]])
```

同样，数组与标量的算术运算也会将那个标量值传播到各个元素

```python
# %%
1 / arr
# array([[1.        , 0.5       , 0.33333333],
#        [0.25      , 0.2       , 0.16666667]])
# %%
arr ** 0.5
# array([[1.        , 1.41421356, 1.73205081],
#        [2.        , 2.23606798, 2.44948974]])
```

不同大小的数组之间的运算叫做广播。

### 基本的索引和切片

NumPy数组的索引是一个内容丰富的主题，因为选取数据子集或单个元素的方式有很多。一维数组很简单。从表面上看，它们跟Python列表的功能差不多。

```python
# %%
arr = np.arange(10)
arr
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# %%
arr[5]
# 5
# %%
arr[5:8]
# array([5, 6, 7])
# %%
arr[5:8] = 12
arr
# array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])
```

当你将一个标量赋值给一个切片时，该值会自动传播到整个选区。跟列表最重要的区别在于，数组切片是原始数组的视图。这意味着数据不会被复制，视图上的任何修改都会直接反映到原数组上。

```python
# %%
arr_slice = arr[5:8]
arr_slice[1] = 12345
arr
# array([    0,     1,     2,     3,     4,    12, 12345,    12,     8,
#            9])
# %%
arr_slice[:] = 64
arr
# array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])
```

由于NumPy的设计目的是处理大数据，如果将数据复制的化会产生性能和内存问题。

对于高维数组，能做的事情更多。在一个二维数组中，各索引位置上的元素不再是标量而是一维数组。

```python
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr2d[1]
#array([4, 5, 6])
```

因此可以对各个元素进行递归访问，但这样需要做的事情有点多。你可以传入逗号隔开索引列表来选取单个元素。

```python
arr2d[0,2]
#3
arr2d[0,2]
#3
```

在多维数组中，如果省略了后面的索引，则返回对象是维度低一点的ndarray。

标量值和数组都可以赋值给高维数组

```python
#%%
arr2d[1]=1
arr2d
#array([[1, 2, 3],
    #    [1, 1, 1]])

#%%
arr2d[1]=arr2d[0].copy()
#array([[1, 2, 3],
    #    [1, 2, 3]])
```

### 切片索引

ndarray的切片语法跟Python列表这样的一维对象差不多：

```python
arr[1:6]
#array([1,2,3,4,5])
```

对于高维数组，切片是沿着一个轴的方向上去元素

```python
arr2d[:1]
#array([[1,2,3]])
arr2d[:1,1:]
#array([[1,2]])
```

向这样进行切片时，只能得到相同维度的数组视图。通过讲整数索引和切片混合，可以得到低纬度的切片。

```python
arr2d[1,:2]
#array([4,5])
arr2d[1,:1]
#array([4])
```

注意，”只有冒号“表示选取整个轴。

### 布尔型索引