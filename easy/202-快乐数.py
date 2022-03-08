class Solution:
    def isHappy(self, n):
        rs = 0
        while 1:
            if rs == 1:
                return True
            rs = 0
            for i in str(n):
                rs = (int(i) ** 2) + rs
                n = rs
            print(rs)
        # return False

s = Solution()
print(s.isHappy(2))