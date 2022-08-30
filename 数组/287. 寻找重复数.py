class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ix = 0
        while ix < len(nums):
            # print(ix, nums)
            if ix + 1 == nums[ix]:
                ix += 1
                continue
            val = nums[ix]
            if val <= ix or nums[ix] == nums[val - 1]:
                return val
            nums[ix], nums[val - 1] = nums[val - 1], nums[ix]
        # print(nums)

nums = [1, 3, 3]
s = Solution()
print(s.findDuplicate(nums))
