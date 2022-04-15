class Solution:
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            nums.append(i)

        rs = 0
        for i in nums:
            rs ^= i

        return rs


s = Solution()
nums = [0]
print(s.missingNumber(nums))