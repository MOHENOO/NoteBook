# 流畅的python

## 魔术方法

### 魔术方法(magic method)

- **len**,**getitem**(可迭代)

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

- **repr**(字符串表示形式),**abs**(绝对值，若为复数，返回模),**add**(+),**mul**(*)

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

[**repr**和**str**区别](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr)

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

+=对应特殊方法**iadd**,若一个类没有实现，则调用**add**。 对可变序列一般都实现了**iadd**方法，+=是就地加法 不可变序列不支持这个操作，调用**add**。 对不可变类型重复拼接操作效率低，每次都需要先把原来对象中的元素先复制到新对象，然后追加新的元素 str类型例外，CPython对其进行了优化，预留了可扩展空间

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

标准库中所有映射类型都是利用dict来实现。所有它们有共同的限制，即只有可散列的数据类型才能用作映射里的键 如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变的，而且这个对象需要实现**hash**()方法.另外可散列对象还有有**qe**()方法，这样才能和其他键比较。 原子不可变数据类型(str,bytes和数值类型)都是可散列类型，forzenset也是可散列类型。元组的话，只有当一个元组包含的所有元素都是可散列类型，它才是可散列的

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

```python
DIAL_CODES = [(86, 'China'), (91, 'India'), (1, 'United States'), (62, 'Indonesia'), (55, 'Brazil'), (92, 'Pakistan'), (880, 'Bangladesh'), (234, 'Nigeria'), (7, 'Russia'), (81, 'Japan'), ]

country_code={country:code for code,country in DIAL_CODES} 
country_code 
#{'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55, 'Pakistan': 92, 'Bangladesh': 880, 'Nigeria': 234, 'Russia': 7, 'Japan': 81}
{code:country.upper() for country,code in country_code.items() if code<66}
# {1: 'UNITED STATES', 62: 'INDONESIA', 55: 'BRAZIL', 7: 'RUSSIA'}
```

### 常见的映射方法

- setdefault

使用get()

```python
import sys import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.findite(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

for word in sorted(index, key=str.upper):
     print(word, index[word]

# 输出每一行列表都表示一个单词的出现情况，第一个值是出现的行，第二个值是出现的列
```

使用setdefault()替代get()

```python
import sys 
import re

WORD_RE = re.compile(r'\w+')

index = {} with open(sys.argv[1], encoding='utf-8') as fp:
for line_no, line in enumerate(fp, 1):
    for match in WORD_RE.finditer(line):
        word = match.group()
        column_no = match.start()+1
        location = (line_no, column_no)
        index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
```

也就是说:

```python
my_dict.setdefault(key,[]).append(new_value)
```

相当于：

```python
if key not in my_dict:
    my_dict[key]=[]
my_dict[key].append(new_value)
```

### 映射的弹性键查询

- defaultdict

```python
import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
```

- /_/_missing__

```python
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

def get(self, key, default=None):
    try:
        return self[key]
    except KeyError:
        return default

def __contains__(self, key):
    return key in self.keys() or str(key) in self.keys()
```

所有的映射类型在处理找不到的键的时候，就会调用**missing**()方法，基类dict并没有定义这个刚噶，如果一个类继承了dict，然后实现**missing**()方法，就可以实现设置默认值。

### 字典的变种

- collections.OrderedDict

该类型添加键的时候保持顺序。 popitem()方法默认删除并返回字典最后一个元素 popitem(last=False)调用时删除并返回第一个元素

- collections.ChainMap

该类型可以容纳数个不同的映射对象，然后在进行键查找操作的时候，这些对象会被当做一个整体被逐个查找，直到键被找到。

- collections.Counter

这个映射类型会给键准备一个整数计数器。每次更新一个键的时候都会增加这个计数器。

```python
import collections
ct=collections.Counter('abracadabra')
ct
#Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.update('aaaaazzz')
ct
Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.most_common(2)
#[('a', 10), ('z', 3)]
```

- collections.UserDict

让用户继承的字典类，但UserDict并不是dict的子类.

```python
import collections
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)]=item
```

键为字符串的字典

### 不可变映射类型

- types.MappingProxyType

如果给这个类一个映射，它会返回一个只读的映射视图。

```python
from types import MappingProxyType
d = {1: 'A'}
d_proxy=MappingProxyType(d)
#mappingproxy({1: 'A'})
d_proxy d_proxy[1]
#'A'
d_proxy[2] = x
#Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# NameError: name 'x' is not defined</module></stdin>

d[2]='B'
# mappingproxy({1: 'A', 2: 'B'})
d_proxy d_proxy[2]
# 'B'
```

### 集合论

集合的本质是许多唯一对象的聚集。因此集合可以用来去重。

集合中的元素必须是可散列的，set类型本身是不可散列的，但frozenset可以。因此可以创建一个包含不同frozenset的set。

a|b返回的是它们的合集。a&b得到交集。a-b差集。

- 集合字面量

如果是空集，那么必须写成set()的形式。除空集外，集合的字面量{1},{1,2}

```python
s={1}
type(s)
# <class 'set'>
s
#{1}
s.pop()
#1
s
#set()
```

由于Python里没有针对frozenset的特殊字面量句法，我们只能采用构造方法。

- 集合推导

```python
from unicodedata import name
{chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
#{'§', '>', '¥', '=', '#', '+', 'µ', '£', '©', '%', '®', '¢', '¤', '×', '÷', '¬', '$', '±','°', '<', '¶'}
```

### dict和set的背后

- 字典中的散列表

散列表其实是一个稀疏数组(总有空白元素的数组)。散列表的单元叫做表元。在dict的散列表中，每个键值对占用一个表元，每个表元都有两个部分,一个是对键的引用，另一个是对值的引用。

为了让散列表能够胜任散列表索引这一角色，它们必须在索引空间中尽量分散开。这意味这在最理想的状况下，越是相似但不相等的对象，它们的散列值的差别应该越大。

```python
hash(1)
# 1
hash(1.0)
# 1
hash(1.0001)
# 230584300921345
```

- dict或set的实现及其导致的结果
1. 键必须是可散列的
2. 支持通过__eq__()方法来检测相等性
3. 若a==b为真,则hash(a)==hash(b)也为真
4. 字典或集合在内存上的开销巨大
5. 键查询很快
6. 键的次序取决于添加顺序
7. 往字典或集合里添加新键可能会改变已有键的顺序

所有用户自定义对象默认都是可散列的，因为它买二散列值由id()来获取

## 文本和字节序列

### 字符编码和解码

把码位转换成字节序列的过程是编码；把字节序列转换成码位的过程是解码。

把字节序列变成人类可读的文本字符串就是解码(decode)，把字符串变成用于存储或传输的字节序列就是编码(encode)。

**python2**的str对象获取的是原始字符序列

**python3**的str类型基本相当于python2的unicode类型，不过python3的bytes类型却不是把str类型换个名称那么简单，而且还有关系紧密的bytearray类型。

```python
s='cafe'
len(s)
#4
b=s.encode('utf16')
b
#b'\xff\xfec\x00a\x00f\x00e\x00'
len(b)
#10
b.decode('utf16')
#cafe
```

### 字节概要

- 概要

python内置了两种基本的二进制序列类型：python3引入不可变bytes类型，python2.6添加可变bytearray类型。(python2.6也引入了bytes类型，但不过是str类型的别名,与python3的bytes类型不同)

bytes或bytearray对象各个元素介于0~255(含)之间的整数，而不是像python2的str对象那样是单个的字符。二进制序列的切片始终是同一类型的二进制序列，包括长度为1的切片。

```python
cafe=bytes('cafe',encoding='utf-8')
cafe
#b'cafe'
cafe[0]
#bytes对象的各个元素都是range(256)内的整数 99
cafe[:1]
#bytes对象的切片还是bytes对象，即使是只有一个字节的切片 b'c'
cafe_arr=bytearray(cafe)
cafe_arr
#bytearray对象没有字面量句法,而是以bytearray()和字节序列字节量参数的形式显示 bytearray(b'cafe')
cafe_arr[-1:]
#bytearray对象的切片还是bytearray对象 bytearray(b'e')
```

s[0]==s[:1]只对str这个序列类型成立。对其他序列类型来说，s[i]返回一个元素，而s[i:i+1]返回一个相同类型的序列。

虽然二进制序列其实是整数序列，但是它们的字面量表示发表明其中有ASCII文本。

可打印的ASCII范围内的字节(从空格到~),使用ASCII字符本身。

制表符,换行符,回车符和\对应的字节，使用转义序列\t,\n,\r和\\\\。

其他字节的值，使用十六进制转义序列。

- 结构体和内存试图

struct模块提供了一些函数，把打包的字节序列转换成不同类型字段组成的元组，还有一些函数用于执行反向转换，把元组转换成打包的字节序列。struct模块能处理bytes，bytearray和memoryview对象。

memoryview类不是用于创建或存储字节序列的，而是共享内存，让你访问其他二进制序列，打包的数组和缓冲中的数据切片，而无需复制字节序列。

```python
import struct
fmt = '<3s3sHH'
#结构体的格式:<是小字节序，3s3s是两个3字节序列，HH是两个16位二进制整数。
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())
    header = img[:10]
    #用memoryview对象的切片新建一个memoryview对象，这里不会复制字节序列。
    bytes(header)
    # b'GIF89a+\x02\xe6\x00
    struct.unpack((fmt, header))
    # (b'GIF',b'89a',555,230) 拆包memoryview对象，得到一个元组，包含类型，版本，宽度和高度。
    del header
    #删除引用，释放memoryview实例所占的内存。
    del img
```

### 基本的编解码器

python自带了超过100种编解码器，用于在文本和字节之间相互转换。每个编解码器都有一个名称，如'utf_8',而且经常有几个别名，如'utf-8'和'U8'。这些名称可以传给open(),str.encode(),bytes.decode()等函数的encoding参数。

```python
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec,'El Nino'.encode(codec),sep='\t')
# latin_1 b'El Nino'
# utf_8   b'El Nino'
# utf_16  b'\xff\xfeE\x00l\x00 \x00N\x00i\x00n\x00o\x00'
```

### 了解编解码问题