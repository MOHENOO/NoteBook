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
