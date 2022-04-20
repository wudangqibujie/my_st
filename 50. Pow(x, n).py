class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x, n - 1)


s = Solution()
x = 2.10000
n = 200000000
print(s.myPow(x, n))