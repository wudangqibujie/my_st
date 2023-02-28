class Solution:
    def firstMissingPositive(self, nums):
        log = dict()
        for i in nums:
            log[i] = True
        i = 1
        while i in log:
            i += 1
        return i


s = Solution()
nums = [7,8,9,11,12]
print(s.firstMissingPositive(nums))