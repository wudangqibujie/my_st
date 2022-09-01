class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(len(prices))] for _ in range(4)]
        dp[0][0] = float("-inf")
        dp[1][0] = 0
        dp[2][0] = 0 - prices[0]
        dp[3][0] = float("-inf")
        # for i in dp:
        #     print(i)
        for t in range(1, len(prices)):
            dp[0][t] = max(dp[0][t - 1], dp[2][t - 1])
            dp[1][t] = max(dp[1][t - 1], dp[3][t - 1])
            dp[2][t] = max(dp[1][t - 1], dp[3][t - 1]) - prices[t]
            dp[3][t] = max(dp[0][t - 1], dp[2][t - 1]) + prices[t]
        for i in dp:
            print(i)
        return max([dp[1][-1], dp[3][-1]])


print(max([float("-inf"), 3]))
nums = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(nums))