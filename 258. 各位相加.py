
class Solution:
    def addDigits(self, num):
        num_str = str(num)
        while len(num_str) > 1:
            rs = 0
            for i in num_str:
                rs += int(i)
            num_str = str(rs)
        return int(num_str)


s = Solution()
print(s.addDigits(78))