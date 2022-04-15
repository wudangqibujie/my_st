class Solution:
    def numberOfArithmeticSlices(self, nums):
        pre = [None]
        dp = [0 for _ in range(len(nums))]
        if len(nums) < 3:
            return 0
        for ix in range(1, len(nums)):
            pre.append(nums[ix] - nums[ix - 1])
        for ix in range(2, len(nums)):
            if pre[ix] == pre[ix - 1]:
                dp[ix] = dp[ix - 1] + 1
            else:
                dp[ix] = 0
        return sum(dp)


s = Solution()
nums = [1, 2, 3, 11, 13, 15, 17]
print(s.numberOfArithmeticSlices(nums))