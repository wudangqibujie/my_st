
class Solution:
    def maxSubArray(self, nums):
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                if dp[i - 1] > 0:
                    dp[i] = nums[i] + dp[i - 1]
                else:
                    dp[i] = nums[i]
            else:
                if dp[i - 1] < 0:
                    dp[i] = nums[i]
                else:
                    dp[i] = dp[i - 1] + nums[i]
        # print(dp)
        return max(dp)


s = Solution()
nums = [5,4,-1,7,8]
print(s.maxSubArray(nums))