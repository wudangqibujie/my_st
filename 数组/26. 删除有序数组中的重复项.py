class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i, j = 1, 0
        lst = nums[j]
        while j < len(nums):
            if nums[j] == lst:
                j += 1
                continue
            nums[i] = nums[j]
            lst = nums[j]
            i += 1
            j += 1
        print(nums, i)
        return i


nums = [0]
s = Solution()
s.removeDuplicates(nums)