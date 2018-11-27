2. 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

解法一(效率低):

```python
    def replaceSpace(self, s):
    # write code here
    result=''
    for i in s:
        if i==' ':
            result+='%20'
        else:
            result+=i
    return result
```

解法二(自带函数):

```python
	def replaceSpace(self,s):
	 # write code here
	return s.replace(' ','%20')
```

3. 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。


```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result=[]
        while listNode:
            result.append(listNode.val)
            listNode=listNode.next
        return result[::-1]
```

若在原链表上修改。

```python
def printListFromTailToHead(self, listNode):
    # write code here
    if(listNode==None or listNode.next==None):
        return listNode
    p1,p2=listNode,listNode.next
    while p2:
        p3=p2.next
        p2.next=p1
        p1=p2
        p2=p3

    listNode.next=None
    listNode=p1
    return listNode
```

4. 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==0:
            return None
        if len(pre)==1:
            return TreeNode(pre[0])
        else:
            root=TreeNode(pre[0])
            root.left=self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1],tin[:tin.index(pre[0])+1])
            root.right=self.reConstructBinaryTree(pre[tin.index(pre[0])+1:],tin[tin.index(pre[0])+1:])
            return root
```

5. 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.Stack1 = []
        self.Stack2 = []

    def push(self, node):
        # write code here
        self.Stack1.append(node)

    def pop(self):
        # return xx
        if self.Stack2 == []:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())
            return self.Stack2.pop()
        return self.Stack2.pop()
```

6.
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

```python
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        for i in range(0, len(rotateArray) - 1):
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]
```

7. 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

```python
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

```

8. 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

```python
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        a, b = 1, 1
        for i in range(number):
            a, b = b, a + b
        return a
```

Exam: 1,2,3,5

9. 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。


```python
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number - 1)
```

Exam:1,2,4,8

10. 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

```python
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        a, b = 1, 1
        for i in range(number):
            a, b = b, a + b
        return a
```
Exam:0,1,2,3,5

11. 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

```python
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while n&0xffffffff != 0:
            count += 1
            n = n & (n-1)
        return count
```
相邻两数只有一位不同，相与后最低位1变为0，实现计数1。
python3 int类型无长度限制。人为通过与0xffffffff(二的32次方-1)相与实现位数限制。

12. 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

```python
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        return base**exponent
```

13. 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

```python
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        return [i for i in array if i%2!=0]+[j for j in array if j%2==0]
```

14. 输入一个链表，输出该链表中倒数第k个结点。

```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if(head is None or head.next is None):
            return head
        p1, p2 = head, head.next
        while p2:
            p3 = p2.next
            p2.next = p1
            p1, p2 = p2, p3
        head.next = None
        result = p1
        for i in range(1, k):
            result = result.next
        return result
```
