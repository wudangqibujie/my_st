class Solution:
    def numTrees(self, n):
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        def helper(i, j):
            if i >= j:
                return 1
            # print(i, j)
            if dp[i][j] != 0:
                return dp[i][j]
            rs = 0
            for idx in range(i, j):
                rs += (helper(i, idx) * helper(idx + 1, j))
            dp[i][j] = rs
            return rs

        return helper(0, n)


s = Solution()
print(s.numTrees(19))