# 排序算法
## 直接选择排序

```python
def select_sort(a):
    count=len(a)
    for i in range(count):
        min=i
        for j in range(i+1,count):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
    return a

print(select_sort([5,3,4,2,1]))
```

最好情况：正序有序，交换0次，但是每次都要找到最小元素，因而只是减少了交换次数，时间复杂度为O(n^2)，最坏情况：时间复杂度为O(n^2).空间复杂度为O(1)，不需要辅助空间。平均情况下：O(n^2)。稳定性：不稳定，例如5，8，5，2，9,第一次选择后交换5,2改变了两个5的先后位置。

## 冒泡排序

```python
def bubble_sort(a):
    count=len(a)
    for i in range(count):
        for j in range(count-1,i,-1):
            if a[j]<a[j-1]:
                a[j],a[j-1]=a[j-1],a[j]
    return a

print(bubble_sort([5,4,3,2,1]))
```



最好情况：正序有序，交换0次，时间复杂度为O(n)，最坏情况：逆序有序，时间复杂度为O(n^2).空间复杂度为O(1)，不需要辅助空间。平均情况下：O(n^2)。稳定性：稳定，每次只交换相邻逆序数

## 插入排序

```python
def insertion_sort(a):
    count=len(a)
    if count==1:
        return a
    for j in range(1,count):
        i=j-1
        temp=a[j]
        while i>=0 and temp<a[i]:
            a[i+1]=a[i]
            i-=1
        a[i+1]=temp
    return a

print(insertion_sort([5, 4, 3, 2, 1]))
```

最好情况：正序有序，比较n次，时间复杂度为O(n)，最坏情况：逆序有序，每次比较n-1次，时间复杂度为O(n^2).空间复杂度为O(1)，不需要辅助空间。平均情况下：O(n^2)。稳定性：稳定，相同数字不需要插入。

## 快速排序

```python
def quick_sort(a,start,end):
    if(start>=end):
        return
    m=a[start]
    left,right=start,end
    while(left<right):
        while a[right]>m and left<right:
            right-=1
        while a[left]<m and left<right:
            left+=1
        a[left],a[right]=a[right],a[left] #左右分别逼近
    print(a)
    quick_sort(a,start,left-1)
    quick_sort(a,right+1,end)

quick_sort([6,5,4,2,1,3],0,5)
```

最好情况：数组递归过程中基本平衡（树），时间复杂度为O(nlogn)，空间复杂度O(logn)。最坏情况：数组有序，时间复杂度为O(n^2).空间复杂度为O(n).平均情况下：时间复杂度O(nlogn),空间复杂度O(logn),由递归产生。稳定性：不稳定。

## 希尔排序

```python
def shell_sort(a):
    count=len(a)
    n=count//2 #步长
    while n>0:
        for i in range(n,count): #步长进行插入排序
            j=i
            temp=a[i]
            while j>=n and a[j-n]>temp:
                a[j]=a[j-n]
                j-=n
            a[j]=temp
        n=n//2
    return a

print(shell_sort([5,4,3,2,1]))
```

最好情况：数组基本有序，时间复杂度为O(n^1.3),接近与插入排序。最坏情况：数组无序，时间复杂度为O(n^2).平均情况下：时间复杂度O(nlogn)~O(n^2),空间复杂度O(1)。稳定性：不稳定。步长内排序，会改变同值元素顺序

## 归并排序

```python
def merge_sort(a):
    count=len(a)
    if count<=1:
        return a

    def merge(left,right):
        result=[]
        l,r=0,0
        while l<len(left) and r<len(right):
            if left[l]<right[r]:
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r+=1

        result+=left[l:]
        result+=right[r:]
        return result

    mid=count//2
    left=merge_sort(a[:mid])
    right=merge_sort(a[mid:])
    return merge(left,right)

print(merge_sort([5,4,3,2,1]))
```

最好情况,最坏情况：时间复杂度O(nlogn)，空间复杂度O(n) 稳定性：稳定。

## 堆排序

```python
def heap_sort(a):
    def sift_down(start,end):
        root=start
        while True:
            child=2*root+1
            if child>end:
                break
            if child+1<=end and a[child]<a[child+1]:
                child+=1
            if a[root]<a[child]:
                a[root],a[child]=a[child],a[root]
                root=child
            else:
                break

    length=len(a)

    #创建最大堆
    for start in range(length//2,-1,-1):
        sift_down(start,length-1)

    for end in range(length-1,0,-1):
        a[0],a[end]=a[end],a[0]
        sift_down(0,end-1)
    return a

print(heap_sort([5,4,3,2,1]))
```

时间复杂度:最好，最坏O(logn),在构建堆的过程中，完全二叉树从最下层最右边的非终端结点开始构建，将它与其孩子进行比较和必要的互换，对于每个非终端结点来说，其实最多进行两次比较和互换操作，因此整个构建堆的时间复杂度为O(n)。
 在正式排序时，第i次取堆顶记录重建堆需要用O(logi)的时间（完全二叉树的某个结点到根结点的距离为⌊log2i⌋+1），并且需要取n-1次堆顶记录，因此，重建堆的时间复杂度为O(nlogn)。

## 计数排序

计数排序是一种稳定的线性时间排序算法。计数排序使用一个额外的数组C，其中第i个元素是待排序数组A中值等于i的元素的个数。然后根据数组C来将中的元素排到正确的位置。
