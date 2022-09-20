class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        print(nums)
        rs = [None for _ in range(len(nums))]
        ix = 0
        cx = 0
        while ix < len(nums):
            rs[ix] = nums[cx]
            cx += 1
            ix += 2
        print(rs)
        while cx < len(nums):
            ix = len(rs) - 1
            while rs[ix]:
                ix -= 1
            rs[ix] = nums[cx]
            cx += 1
        for ix , i in enumerate(rs):
            nums[ix] = i





nums = [4,5,5,6]

s = Solution()
s.wiggleSort(nums)
print(nums)