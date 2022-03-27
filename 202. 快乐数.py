class Solution:
    def isHappy(self, n):
        readed = set()
        while n not in readed:
            readed.add(n)
            rs = 0
            for i in range(len(str(n))):
                rs += (int(str(n)[i]) ** 2)
            n = rs
            if n == 1:
                return True
        return False



s = Solution()
print(s.isHappy(10000))



