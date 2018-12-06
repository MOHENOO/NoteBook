# 流畅的python

## 魔术方法

### 魔术方法(magic method)

- __len__,__getitem__(可迭代)

```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
# namedtuple 构建只有少数属性但没方法的对象


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.sults for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
```

- __repr__(字符串表示形式),__abs__(绝对值，若为复数，返回模),__add__(+),__mul__(*)

```python
from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({},{})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


    def __add__(self, other):
        x = self.x + other.x
        y = self.x + other.x
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
```

[__repr__和__str__区别](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr)

## 序列

### 列表推导和生成器表达式

- 列表推导

```python
num=[i for i in range(10)]
```

- 笛卡尔积

```python
colors=['black','white']
sizes=['S','M','L']
tshirts=[(color,size)
        for color in colors for size in sizes]
```

- 生成器表达式(逐个产生对象，节省内存)

```python
colors=['black','white']
sizes=['S','M','L']
tshirt=((color,size) for color in colors for size in sizes)
```

### 元组(tuple)

- 元组和记录 元组中每个元素都存放了记录中一个字段的数据，外加这个字段的位置

- 元组拆包

```python
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
#东京市的市名，年份，人口，人口变化，面积
```

元素数目一致，用*处理多余元素

```python
a,b,*rest=range(5)
#>>>a,b,rest
#(0,1,[2,3,4])
a,*body,c,d=range(5)
#>>a,body,c,d
#(0,[1,2],3,4)
```

- 具名元组(collections.namedtuple)

```python
Card = collections.namedtuple('Card', ['rank', 'suit'])
```

_fields()类属性，类方法

\_make(iterable)接收一个可迭代对象生成这个类的实例，类似通过_变量。

_asdict()通过collections.OrderDict形式返回

### 切片

- 多维切片 Python 内置的序列类型都是一维的，numpy中可以使用多维切片。

- 省略(三个英文句号)

```python
a[i:...]
#若a是四维数组，相当于a[i:,:,:]
```

...用作多维数组切片的快捷方式。

- 切片赋值

```python
l = list(range(10))
l[2:5] = [20, 30]
#l=[0, 1, 20, 30, 5, 6, 7, 8, 9]
del(l[5:7])
#[0, 1, 20, 30, 5, 8, 9]
l[2:5] = 100
#错误
l[2:5] = [100]
#正确，切片赋值右侧必须是可迭代对象
```

### 序列+和*

- *和+ 不修改原有操作对象，而是构建一个新的序列

```python
board = [['_'] * 3 for i in range(3)]
#[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 'X'
#正确[['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]

weird_board=[['_']*3]*3
#[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
weird_board[1][2]='0'
#错误[['_', '_', '0'], ['_', '_', '0'], ['_', '_', '0']]
```

weird_board中外面的列表其实包含3个指向同一个列表的引用，所有3个列表都修改

- 序列的增量赋值(+=和*=)

```python
l=[1,2,3]
id(l)
#4464682376
l*=2
id(l)
#4464682376
t=(1,2,3)
id(t)
#4464207192
t+=(2)
id(t)
#4464499880
```

+=对应特殊方法__iadd__,若一个类没有实现，则调用__add__。 对可变序列一般都实现了__iadd__方法，+=是就地加法 不可变序列不支持这个操作，调用__add__。 对不可变类型重复拼接操作效率低，每次都需要先把原来对象中的元素先复制到新对象，然后追加新的元素 str类型例外，CPython对其进行了优化，预留了可扩展空间

```python
t=(1,2,[30,40])
# (1, 2, [30, 40])
t[2]+=[50,60]
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-3-a869e900fa6a> in <module>
# ----> 1 t[2]+=[50,60]
#
# TypeError: 'tuple' object does not support item assignment
print(t)
#(1, 2, [30, 40, 50, 60])
```

### 排序序列

- 排序 list.sort()和内置函数sorted() list.sort()就地排序列表，返回值None 可迭代对象sorted()新建一个排序后列表做返回值 均包含参数reverse，key

- bisect bisect,insort利用二分查找来在有序序列中查找或插入元素

### 数组(array.array)

- 数组存入文件和读取

```python
from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
# 0.6338467182200953
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
# 0.6338467182200953
print(floats2 == floats)
# True
```

### 内存视图(memoryview)

```python
from array import array

numbers = array('h', [-2, -1, 0, 1, 2])
#'h' 短整型有符号整数，占两个字节
memv = memoryview(numbers)
print(len(memv))
#5
print(memv[0])
#-2
memv_oct = memv.cast('B')
#'B' 无符号字符
print(memv_oct.tolist())
#[254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
#每两位对应一个有符号短整数，高位为数值位，低位为符号位
memv_oct[5] = 4
print(numbers)
# array('h', [-2, -1, 1024, 1, 2])
```

### NumPy和SciPy 科学计算库

### 队列

- 双向队列和其他形式队列 collections.deque(双向队列，线程安全)

```python
from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.rotate(3)
print(dq)
# deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
dq.rotate(-4)
print(dq)
# deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
dq.appendleft(-1)
print(dq)
# deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.extend([11, 22, 33])
print(dq)
# deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
dq.extendleft([10, 20, 30, 40])
print(dq)
# deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)
```

maxlen可容纳元素数量 rotate队列的旋转操作

标准库queue multiprocessing.queue asyncio.queue异步 heapq 可将可变序列当作堆队列或者优先队列

## 字典和集合

### 泛映射类型

collections.abc中的MutableMapping和Mapping抽象基类。作用是为dict和其他类似的类型定义形式接口

```python
from collections import abc

my_dict = {}
isinstance(my_dict, abc.Mapping)
#True
```

标准库中所有映射类型都是利用dict来实现。所有它们有共同的限制，即只有可散列的数据类型才能用作映射里的键 如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变的，而且这个对象需要实现__hash__()方法.另外可散列对象还有有__qe__()方法，这样才能和其他键比较。 原子不可变数据类型(str,bytes和数值类型)都是可散列类型，forzenset也是可散列类型。元组的话，只有当一个元组包含的所有元素都是可散列类型，它才是可散列的

```python
tt = (1, 2, (30, 40))
hash(tt)
t1 = (1, 2, [30, 40])
hash(t1)
#Error ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-13-9d6f6e59c7bb> in <module>
#       2 hash(tt)
#       3 t1 = (1, 2, [30, 40])
# ----> 4 hash(t1)
#
# TypeError: unhashable type: 'list'
```

### 字典创建方法

```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e
#True
```

### 字典推导
