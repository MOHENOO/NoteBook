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
