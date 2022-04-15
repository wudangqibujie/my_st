class Solution:
    def hasAlternatingBits(self, n):
        print(bin(n))
        ans = []
        while n != 0:
            ans.append(int(n % 2 == 0))
            n = n >> 1
        for i in range(1, len(ans)):
            if abs(ans[i] - ans[i - 1]) != 1:
                return False
        return True



s = Solution()
print(s.hasAlternatingBits(5))
