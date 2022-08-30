class Solution:
    def findMin(self, nums):
        i, j = 0, len(nums) - 1
        while True:
            # print(i, j)
            if (j - i) <= 2:
                return min(nums[i: j + 1])
            mid = (i + j) // 2
            if nums[mid] > nums[j]:
                i = mid
            else:
                j = mid


s = Solution()
nums = [19, 11,13,15,17]
print(s.findMin(nums))