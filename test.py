class Solution:
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        # 对array中的数字进行异或运算
        sum = 0
        for i in array:
            sum ^= i
        index = 0
        while (sum & 1) == 0:
            sum >>= 1
            index += 1
        a = b = 0
        for i in array:
            if self.fun(i, index):
                a ^= i
            else:
                b ^= i
        return [a, b]

    def fun(self, num, index):
        num = num >> index
        return num & 1
