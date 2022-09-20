class Solution:
    def change(self, amount, coins):
        dp = [[0 for _ in range(len(coins) + 1)] for _ in range(amount + 1)]
        dp[0] = [1 for _ in range(len(coins) + 1)]
        for i in range(1, amount + 1):
            for j in range(1, len(coins) + 1):
                rs1 = dp[i][j - 1]
                # print(j)
                # print(i - coins[j])
                if i - coins[j - 1] >= 0:
                    rs2 = dp[i - coins[j - 1]][j]
                else:
                    rs2 = 0
                dp[i][j] = rs1 + rs2
        # for i in dp:
        #     print(i)
        return dp[-1][-1]

s = Solution()
amount = 5
coins = [2, 1, 5]
# amount = 3
# coins = [2]
amount = 4
coins = [2, 1]
print(s.change(amount, coins))