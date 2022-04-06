class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        ix = len(nums) - 2

        while ix >= 0 and nums[ix] >= nums[ix + 1]:
            ix -= 1
        if ix == -1:
            nums.reverse()
            return
        jx = len(nums) - 1
        while jx >= 0 and nums[jx] <= nums[ix]:
            jx -= 1
            print(jx)
        print(ix, jx)
        nums[ix], nums[jx] = nums[jx], nums[ix]
        print(nums)

        i, j = ix + 1, len(nums) - 1
        print("START", i, j)
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        print(nums)





s = Solution()
num = [5, 1, 1]
s.nextPermutation(num)




