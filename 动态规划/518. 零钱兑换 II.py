class Solution:
    def change(self, amount, coins):
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        coins = [None] + coins

        for i in range(1, amount + 1):
            for j in range(1, len(coins) + 1):
                add1 = dp[i - 1][j - coins[i]] if j >= coins[i] else 0
                dp[i][j] = add1 + dp[i - 1][j]
            if i == 1:break
        for i in dp:
            print(i)


s = Solution()
amount = 5
coins = [1, 2, 5]
print(s.change(amount, coins))