class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(4)] for _ in range(len(prices))]
        dp[0][1] = float("-inf")
        dp[0][3] = float("-inf")
        dp[0][2] = 0 - prices[0]

        for t in range(1, len(prices)):
            dp[t][0] = max(dp[t - 1][0], dp[t - 1][3])
            dp[t][1] = max(dp[t - 1][1], dp[t - 1][2])
            dp[t][2] = dp[t - 1][0] - prices[t]
            dp[t][3] = max(dp[t - 1][1], dp[t - 1][2]) + prices[t]
        # for i in dp:
        #     print(i)
        return max(dp[-1][0], dp[-1][3])

s = Solution()
prices = [1]
print(s.maxProfit(prices))