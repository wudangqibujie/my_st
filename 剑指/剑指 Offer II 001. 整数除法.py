class Solution:
    def divide(self, a, b):
        rs = 0
        flag = (a > 0) ^ (b > 0)
        a = abs(a)
        b = abs(b)
        while a >= b:
            a -= b
            rs += 1
        rs = -rs if flag else rs
        return rs

s = Solution()
print(s.divide(0, -1))


