class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        print(nums)

        mid = 1
        l, r = 0, len(nums) - 1
        eps = None
        res = None
        while True:

            sum_val = nums[l] + nums[mid] + nums[r]
            if sum_val > target:
                r -= 1
            else:
                l += 1






nums = [-1,2,1,-4]
target = 2
s = Solution()
print(s.threeSumClosest(nums, target))
