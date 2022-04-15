class Solution:
    def minPathSum(self, grid):
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, len(grid[0])):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in dp:
            print(i)
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

s = Solution()
grid = [[1,2],[1,1]]
print(s.minPathSum(grid))

