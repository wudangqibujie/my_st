import numpy as np

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        k = 2
        dp = []
        for _ in range(len(prices)):
            dp.append([[0, k] for _ in range(4)])

nums = [7,1,5,3,6,4]
s = Solution()
s.maxProfit(nums)