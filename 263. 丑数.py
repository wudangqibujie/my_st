class Solution:
    def isUgly(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 1:
            flg = False
            for i in [5, 3, 2]:
                if n >= i and n % i == 0:
                    flg = True
                    n = n // i
                    break

            if not flg:
                return False
        return True

s = Solution()
for i in range(1, 100):
    print(-i, s.isUgly(-i))