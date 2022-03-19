class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        dp = [0 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            candis = []
            for c in coins:
                if i < c:
                    continue
                candis.append(dp[i - c])
            if len(candis) != 0 and sum(candis) != 0:
                dp[i] = min(candis) + 1
            else:
                dp[i] = 0
        print(dp)
        if dp[-1] == 0:
            return -1
        return dp[-1]


s = Solution()
coins = [1, 2, 5]
amount = 11
print(s.coinChange(coins, amount))



