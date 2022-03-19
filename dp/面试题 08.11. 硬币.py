class Solution:
    def waysToChange(self, n):
        coins = [1, 5, 10, 25]
        dp = [[0 for _ in range(n + 1)] for _ in range(4)]
        for i in range(4):
            dp[i][0] = 1
        for i in range(n + 1):
            dp[0][i] = 1


        for i in range(1, 4):
            for j in range(1, n + 1):
                val = coins[i]
                # print(j, val)
                if j < val:
                    addition = 0
                else:
                    # print("异常")
                    addition = dp[i][j - val]
                dp[i][j] = dp[i - 1][j] + addition
        return dp[-1][-1] % 1000000007
s = Solution()
n = 125
print(s.waysToChange(n))
