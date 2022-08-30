class Solution:
    def minSubArrayLen(self, target, nums):
        l = total = 0
        ans = len(nums) + 1
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if ans == len(nums) + 1 else ans




s = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(s.minSubArrayLen(target, nums))