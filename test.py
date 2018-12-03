# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        ss = [str(i) for i in numbers]
        left = self.PrintMinNumber(
            [i for i in ss[1:] if (i + ss[0]) < (ss[0] + i)])
        right = self.PrintMinNumber(
            [i for i in ss[1:] if i + ss[0] >= ss[0] + i])
        return int(''.join(left + [ss[0]] + righ))
