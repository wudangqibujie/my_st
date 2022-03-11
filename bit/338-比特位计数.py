class Solution:
    def countBits(self, n):
        ans = []
        for i in range(n + 1):
            ans.append(self.hammingWeight(i))
        return ans

    def hammingWeight(self, n):
        cnt = 0
        while n != 0:
            cnt += 1
            n = n & (n - 1)
        return cnt


s = Solution()
print(s.countBits(5))
