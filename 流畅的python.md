1.  魔术方法(magic method)

**len**,**getitem**(可迭代)

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

**repr**(字符串表示形式),**abs**(绝对值，若为复数，返回模),**add**(+),**mul**(\*)

[**repr**和**str**区别](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr)

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

2.  列表推导

-   列表推导

```python
num=[i for i in range(10)]
```

-   笛卡尔积

```python
colors=['black','white']
sizes=['S','M','L']
tshirts=[(color,size)
        for color in colors for size in sizes]
```

3.  生成器表达式(逐个产生对象，节省内存)

```python
colors=['black','white']
sizes=['S','M','L']
tshirt=((color,size) for color in colors for size in sizes)
```

4.  元组(tuple)

-   元组和记录
    元组中每个元素都存放了记录中一个字段的数据，外加这个字段的位置
-   元组拆包

```python
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
#东京市的市名，年份，人口，人口变化，面积
```

元素数目一致，用\*处理多余元素

```python
a,b,*rest=range(5)
#>>>a,b,rest
#(0,1,[2,3,4])
a,*body,c,d=range(5)
#>>a,body,c,d
#(0,[1,2],3,4)
```

-   具名元组(collections.namedtuple)

```python
Card = collections.namedtuple('Card', ['rank', 'suit'])
```

\_fields()类属性，类方法

\_make(iterable)接收一个可迭代对象生成这个类的实例，类似通过_变量。

\_asdict()通过collections.OrderDict形式返回

-   作为不可变列表

5.切片

- 多维切片
Python 内置的序列类型都是一维的，numpy中可以使用多维切片。

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

6. 序列
- \*和+
不修改原有操作对象，而是构建一个新的序列
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

- 序列的增量赋值(+=和\*=)
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
+=对应特殊方法__iadd__,若一个类没有实现，则调用__add__。
对可变序列一般都实现了__iadd__方法，+=是就地加法
不可变序列不支持这个操作，调用__add__。
对不可变类型重复拼接操作效率低，每次都需要先把原来对象中的元素先复制到新对象，然后追加新的元素
str类型例外，CPython对其进行了优化，预留了可扩展空间
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

7. 排序序列
- 排序
list.sort()和内置函数sorted()
list.sort()就地排序列表，返回值None
可迭代对象sorted()新建一个排序后列表做返回值
均包含参数reverse，key
- bisect
bisect,insort利用二分查找来在有序序列中查找或插入元素

8. 数组
