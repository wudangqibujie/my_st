class Solution:
    def removeDuplicates(self, nums):
        wrt_idx, i, j = 0, 0, 1
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if (j - i) == 1:
                nums[wrt_idx] = nums[i]
                wrt_idx += 1
            else:
                nums[wrt_idx] = nums[i]
                nums[wrt_idx + 1] = nums[i]
                wrt_idx += 2

            i = j
            j = i + 1
        if i < len(nums):
            if (j - i) == 1:
                nums[wrt_idx] = nums[i]
            else:
                nums[wrt_idx] = nums[i]
                nums[wrt_idx + 1] = nums[i]
            return wrt_idx + 1
        return wrt_idx


nums = []
so = Solution()
print(so.removeDuplicates(nums))