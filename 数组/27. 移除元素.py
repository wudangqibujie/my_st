class Solution:
    def removeElement(self, nums, val):
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] != val:
                i += 1
                continue
            while j > i and nums[j] == val:
                j -= 1
            nums[i] = nums[j]
            i += 1
            j -= 1
        print(nums, i, j)
        return i + 1


nums = [1, 1]
val = 1
s = Solution()
s.removeElement(nums, val)