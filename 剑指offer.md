2.  请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

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

3.  输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

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
    if not listNode or not listNode.next:
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

4.  输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

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

5.  用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

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

6.  把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

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

7.  大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
    n&lt;=39

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

8.  一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

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

9.  一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

```python
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number - 1)
```

Exam:1,2,4,8

10. 我们可以用2_1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2_1的小矩形无重叠地覆盖一个2\*n的大矩形，总共有多少种方法？

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

15. 输入一个链表，反转链表后，输出新链表的表头。

```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if(pHead is None or pHead.next is None):
            return pead
        p1, p2 = pHead, pHead.next
        while p2:
            p3 = p2.next
            p2.next = p1
            p1, p2 = p2, p3
        pHead.next = None
        pHead = p1
        return pHead
```

16. 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        head = ListNode(0)
        result = head
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                head.next = pHead1
                pHead1 = pHead1.next
            else:
                head.next = pHead2
                pHead2 = pHead2.next
            head = head.next

        if pHead1:
            head.next = pHead1
        if pHead2:
            head.next = pHead2
        return result.next
```

归并排序

17. 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not(pRoot1 and pRoot2):
            return False

        result = False
        if pRoot1.val == pRoot2.val:
            result = self.isSubtree(pRoot1, pRoot2)
        if not result:
            result = self.HasSubtree(
                pRoot1.left, pRoot2) | self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def isSubtree(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val == root2.val:
            return self.isSubtree(root1.left, root2.left) & self.isSubtree(root1.right, root2.right)
        return False
```

18. 操作给定的二叉树，将其变换为源二叉树的镜像。

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
```

19. 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

解法一：

```python
def printMatrix(matrix):
    # write code here
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix:
            matrix = list(map(list, zip(*matrix)))
            matrix.reverse()
    return result
```

解法二:

```python
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        m, n = len(matrix[0]), len(matrix)
        result = []
        startx, endx = 0, m - 1
        starty, endy = 0, n - 1
        add = 1
        while m > 0 and n > 0:
            if add == 1:
                for x in range(startx, endx + 1):
                    result.append(matrix[starty][x])
                starty += 1
                n -= 1

                if n > 0:
                    for y in range(starty, endy + 1):
                        result.append(matrix[y][endx])
                    endx -= 1
                    m -= 1
            else:
                for x in range(endx, startx - 1, -1):
                    result.append(matrix[endy][x])
                endy -= 1
                n -= 1
                if n > 0:
                    for y in range(endy, starty - 1, -1):
                        result.append(matrix[y][startx])
                    m -= 1
                startx += 1
            add = -add
        return result
```

20. 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minstack == [] or node < self.min():
            self.minstack.append(node)
        else:
            self.minstack.append(self.min())

    def pop(self):
        # write code here
        if self.minstack == [] or self.stack == []:
            return None
        self.minstack.pop()
        self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minstack[-1]
```

21. 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

```python
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if pushV == [] or len(pushV) != len(popV):
            return False
        stack = []
        while pushV != []:
            if stack == [] or stack[-1] != popV[0]:
                stack.append(pushV.pop(0))
            if stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if stack == popV[::-1]:
            return True
        return False
```

22. 从上往下打印出二叉树的每个节点，同层节点从左至右打印。

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(root):
        # write code here
        result = []
        if not root:
            return result
        queue = [root]
        while queue != []:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
```

层次遍历

23. 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

```python
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        flag_min = True
        maxindex = 0
        for i in range(len(sequence) - 1):
            if sequence[i] > root:
                flag_min = False
                maxindex = i
                break
        if not flag_min:
            for i in range(maxindex, len(sequence) - 1):
                if sequence[i] < root:
                    return False
        return True
```

24. 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

```python
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None

        node = RandomListNode(pHead.label)
        node.next = pHead.next
        node.random = pHead.random
        node.next = self.Clone(pHead.next)

        return node
```

25. 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        result = []
        path = []
        self.dfs(root, expectNumber, result, path)
        result.sort()
        return result

    def dfs(self, root, target, result, path):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and target == root.val:
            result.append(path[:])

        if root.left:
            self.dfs(root.left, target - root.val, result, path)
        if root.right:
            self.dfs(root.right, target - root.val, result, path)

        path.pop()
```

26. 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return

        self.Convert(pRootOfTree.left)
        if not self.listHead:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead
```

27. 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
    输入描述:
    输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

```python
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        result = []
        if not ss:
            return result
        path = ''
        self.part(ss, result, path)
        return sorted(list(set(result)))

    def part(self, ss, result, path):
        if not ss:
            result.append(path)
        else:
            for i in range(len(ss)):
                self.part(ss[:i] + ss[i + 1:], result, path + ss[i])
```

28. 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

```python
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        length = len(numbers)
        dist_num = {}
        for i in numbers:
            if i not in dist_num:
                dist_num[i] = 1
            else:
                dist_num[i] += 1
            if dist_num[i] == (length // 2 + 1):
                return i
        return 0
```

29. 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

堆排序(小根堆)

```python
# -*- coding:utf-8 -*-
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) < k:
            return []
        return heapq.nsmallest(k, tinput)
```

30. HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

```python
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        result, addnum = array[0], array[0]
        for i in array[1:]:
            if addnum < 0:
                addnum = i
            else:
                addnum += i
            if addnum > result:
                result = addnum
        return result
```

31. 求出1 ~ 13的整数中1出现的次数,并算出100 ~ 1300的整数中1出现的次数？为此他特别数了一下1 ~ 13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

```python
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        i = 1
        while i <= n:
            count += (n // i + 8) // 10 * i + (n // i % 10 == 1) * (n % i + 1)
            i *= 10
        return count
```

设定整数点（如1、10、100等等）作为位置点i（对应n的各位、十位
、百位等等），分别对每个数位上有多少包含1的点进行分析。

根据设定的整数位置，对n进行分割，分为两部分，高位n/i，低位n%i
当i表示百位，且百位对应的数>=2,如n=31456,i=100
，则a=314,b=56，此时百位为1的次数有a/10+1=32（最高两位0~31
)，每一次都包含100个连续的点，即共有(a/10+1) _ 100个点的百位
为1

当i表示百位，且百位对应的数为1，如n=31156,i=100
，则a=311,b=56，此时百位对应的就是1，则共有a/10(最高两位0
-30)次是包含100个连续点，当最高两位为31（即a=311），本次只
对应局部点00~56，共b+1次，所有点加起来共有（a/10 _ 10
0）+(b+1)，这些点百位对应为1

当i表示百位，且百位对应的数为0,如n=31056,i=100则a=310,b=5
6，此时百位为1的次数有a/10=31（最高两位0~30）

综合以上三种情况，当百位对应0或>=2时，有(a+8)/10次包含所有10
0个点，还有当百位为1(a%10==1)，需要增加局部点b+1

32. 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

解法一：穷举法
```python
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        ss = [str(i) for i in numbers]
        result = []
        path = ''
        self.part(ss, result, path)
        return min([int(i) for i in result])

    def part(self, ss, result, path):
        if not ss:
            result.append(path)
        else:
            for i in range(len(ss)):
                self.part(ss[:i] + ss[i + 1:], result, path + ss[i])
```

解法二：特定规则的快排
```python
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        ss = [str(i) for i in numbers]
        return int(''.join(self.quicksort(ss)))

    def quicksort(self, ss):
        if len(ss) < 2:
            return ss[:]
        left = self.quicksort([i for i in ss[1:] if (i + ss[0]) < (ss[0] + i)])
        right = self.quicksort([i for i in ss[1:] if i + ss[0] >= ss[0] + i])
        return left + [ss[0]] + right
```

33. 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

```python
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        result = [1]
        t2, t3, t5 = 0, 0, 0
        while len(result) < index:
            minNum = (min(result[t2] * 2, result[t3] * 3, result[t5] * 5))
            if minNum > result[-1]:
                result.append(minNum)
            if (result[-1] == result[t2] * 2):
                t2 += 1
            elif (result[-1] == result[t3] * 3):
                t3 += 1
            else:
                t5 += 1
        return result[-1]
```
