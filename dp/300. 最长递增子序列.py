class Solution:
    def lengthOfLIS(self, nums):
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1
        for i in range(1, len(nums)):
            rs = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    a = dp[j] + 1
                    rs = max(rs, a)
            rs = rs if rs != 0 else 1
            dp[i] = rs
        # print(dp)
        return max(dp)


s = Solution()
nums = [4,10,4,3,8,9]
# nums = [1,3,6,7,9,4,10,5,6]
print(s.lengthOfLIS(nums))