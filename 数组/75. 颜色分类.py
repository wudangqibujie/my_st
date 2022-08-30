class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l_idx, r_idx = 0, len(nums) - 1
        while l_idx < r_idx:
            while l_idx < len(nums) and nums[l_idx] == 0:
                l_idx += 1
            while r_idx >= 0 and nums[r_idx] != 0:
                r_idx -= 1
            if l_idx >= r_idx:
                break
            nums[l_idx], nums[r_idx] = nums[r_idx], nums[l_idx]
        flg = l_idx
        r_idx = len(nums) - 1
        while l_idx < r_idx:
            while l_idx < len(nums) and nums[l_idx] == 1:
                l_idx += 1
            while r_idx >= flg and nums[r_idx] != 1:
                r_idx -= 1
            if l_idx >= r_idx:
                break
            nums[l_idx], nums[r_idx] = nums[r_idx], nums[l_idx]

s = Solution()
import random
# nums = [2,0,2,1,1,0]
nums = [2,0,1]
# random.shuffle(nums)
print(nums)
print(s.sortColors(nums))
print(nums)
