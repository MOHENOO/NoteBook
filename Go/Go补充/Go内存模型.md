# Go内存模型

## 简介

Go的内存模型限定一个条件,对于同一个变量,一个goroutine被保证,读取时可以看到另一个goroutine的写入.即同一变量,在一方写入时,另一方可以同时读.

## 忠告

程序修改被多个foroutine同时访问的数据时,必须序列化访问.(序列化指的是程序运行的正常顺序)

要序列化访问，可以使用channel或其他同步原语（如sync和sync/atomic包中的原语）保护数据。

## 发生之前

在单个goroutine中，读取和写入必须不影响程序本身顺序执行的结果。也就是说，只有当重新排序不改变程序正确执行，编译器和处理器才可以重新排序在单个goroutine中执行的读取和写入。由于这种重新排序，一个goroutine观察到的执行顺序可能与另一个正在执行的goroutine的顺序不同。例如，如果执行了一个goroutine a = 1; b = 2;，则另一个goroutine先观察到b值的更新,然后才是a.

什么是go程序中执行顺序?
如果事件1发生在事件2之前,那么可以得出事件2发生在事件1之后.如果事件1没有发生在事件2之前,也没有发生在事件2之后,那么我们说事件1和事件2是并行的.

在单个goroutine中，执行顺序和程序没有goroutine的执行顺序相同.

当一个goroutine对变量v读时,要允许另一个goroutine对v写,需要满足:

- 读事件R没有发生在写事件W之前
- 没有其他的写事件Wn发生在当前写事件W1之后,读事件R之前

而为了保证读事件R可以观察到写事件W对变量v的更改,需要满足:

- 写事件W发生在读事件R之前.
- 对共享变量V的其他任何写事件,要么发生在W之前,要么发生在R之后.即不能有其他写事件发生在W-R之间,包括与W,R并行(类似数轴上的集合,W,R为空心,在W左,R右)

这对条件和第一对相比,它要求没有其他写事件与W或R同时发生.(两个空心)

在单个goroutine上,没有并发的问题,所有这两组条件中其他写事件不存在,所以这两组条件对这一情况等价.但当多个goroutine访问共享变量v时,根据它们对两组条件的满足,来获取相应的权限.

对共享变量v的默认初始化(即根据类型赋予类型的零值),在内存模型中表现为一次写事件.

对大于单个机器字的值(如32位机上的int64),其读取和写入表现为未指定顺序进行的多个机器子的操作.

## 同步

### 初始化

程序初始化在单个goroutine,但是这个goroutine可能创建其他并发的goroutine.

如果一个包p导入另一个包q,对q的init发生在p的其他操作之前.

主程序main.main()发生在所有引用包和自身的init()完成之后.

### Goroutine的创建

go启动新的goroutine发生在goroutine开始执行之前.例如:

```go
var a string

func f(){
    print(a)
}

func hello(){
    a="hello,world"
    go f()
}
```

### goroutine销毁

goroutine的销毁不保证发生在程序其他事件之前,例如:

```go
var string

func hello(){
    go func(){
        a="hello"
    }()
    print(a)
}
```

print()事件无法保证发生在a="hello"事件发生之后,即无法满足之前事件R观察到事件W的条件(第二组).

如果想实现另一个goroutine观察到goroutine的写事件W,需要使用锁或channel来确保观察条件的满足.

### channel通信

channel是goroutines之间同步的主要方法.特定信道的每个发送者都与这个频道的接收者相匹配,发送者和接收者通常在不同的goroutine上.

缓冲channel的发送发生在接收之前.(创建channel后,因为缓冲区的存在,发送者可以先发送而不需要接收者).缓冲信道在缓冲区已满时发送者阻塞,缓冲区为空时接收者阻塞.缓冲信道创建后,发送者先阻塞,因为创建channel后已经初始化了缓冲区.缓冲区已满,发送者无法放置数据.当接收者消费后,发送者才取消阻塞.
无缓冲信道的接收发生在发送之前.(创建channel后,发送者发送时需要一个接收者消费数据,所以先需要一个接收者),接收者没有数据接收所以先阻塞,等待发送者发送.

```go
var c=make(chan int,10)
var a string

func f(){
    a="hello,world"
    c<-0
}

func main(){
    go f()
    <-c
    print(a)
}
```

在这个示例中,可以替换c<-0为close(c).

```go
var c=make(chan int)
var a string

func f(){
    a="hello,world"
    <-c
}

func main(){
    go f()
    c<-0
    print(a)
}
```

对于缓冲信道,如果缓冲区中已经有数据,则不能保证读事件print(a),发生在写事件a=""之后.

缓冲信道上的第k个接收发生在k+c个发送之前.c为信道容量.类似与信号量的概念.允许最多信道容量大小的gorountine同时并行.当大于容量后的gorountine开始执行后,会被阻塞,从而限制并发.

```go
var limit=make(chan int,3)

func mian(){
    for _,w:=range work{
        go func(w func()){
            limit<-1
            w()
            <-limit
        }(w)
    }
    select{}
}
```

### 锁

sync包实现了两种锁数据类型,sync.Mutex(互斥锁)和sync.RWMutex(读写互斥锁).

对于Mutex类型l.l.Unlock()必须是l已经被锁定,否则会产生一个run-time error,而l.Lock()中L必须是未锁定的,否则阻塞,等待解锁.

```go
var l sync.Mutex
var a string

func f(){
    a="hello,world"
    l.Unlock()
}

func main(){
    l.Lock()
    go f()
    l.Lock()//当l已经被锁定时,再次Lock(),goroutine会阻塞.直至解锁
    print(a)
}
```

对于RWMutex类型的l,l.Lock()用于锁定写入,l.RLock()用于锁定读取,同理l.Unlock()解锁写,l.RUnlock()解锁读.

当有一个goroutine获得写锁定，其它无论是读锁定还是写锁定都将阻塞直到写解锁；当有一个 goroutine获得读锁定，其它读锁定仍然可以继续加读锁；当有一个或任意多个读锁定，写锁定将等待所有读锁定解锁之后才能够进行写锁定。

### Once

sync通过Once类来提供一种安全机制,实现多个goroutine并行,多个goroutine执行once.Do(f),只有第一次将运行f().启用goroutine如果需要执行f(),则需要新的Once实例.

```go
var a string
var once sync.Once

func setup(){
    a="hello,world!"
}

func dopint(){
    once.Do(setup)
    print(a)
}

func twoprint(){
    go dopint()
    go dopint()
}
```

## 错误的同步

**注意**:读事件R可以观察到同时进行的写事件W所写的共享变量.即便发生这种情况后,读事件R之后的其他读事件也可能能观察到W之前的值.而这与直观的理解有所不同.

```go
var a,b int
func f(){
    a=1
    b=2
}
func g(){
    print(b)
    print(a)
}

func main(){
    go f()
    g()
}
```

这个例子中可能发生g()先打印2,然后打印0.