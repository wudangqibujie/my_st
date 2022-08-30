class Solution:
    def singleNumber(self, nums):
        m = dict()
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        for k, v in m.items():
            if v == 1:
                return k
