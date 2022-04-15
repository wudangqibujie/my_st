class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        flag = float("inf")
        rs = 0
        print(nums)
        for ix in range(len(nums) - 2):
            i, j = ix + 1, len(nums) - 1
            while i < j:
                if nums[ix] + nums[i] + nums[j] > target:
                    if abs(nums[ix] + nums[i] + nums[j] - target) < flag:
                        rs = nums[ix] + nums[i] + nums[j]
                        flag = abs(nums[ix] + nums[i] + nums[j] - target)
                    j -= 1
                elif nums[ix] + nums[i] + nums[j] < target:
                    if abs(nums[ix] + nums[i] + nums[j] - target) < flag:
                        rs = nums[ix] + nums[i] + nums[j]
                        flag = abs(nums[ix] + nums[i] + nums[j] - target)

                    i += 1
                else:

                    if abs(nums[ix] + nums[i] + nums[j] - target) < flag:
                        rs = nums[ix] + nums[i] + nums[j]
                        flag = abs(nums[ix] + nums[i] + nums[j] - target)

        return rs


s = Solution()
nums = [1,1,1,0]
target = -100
print(s.threeSumClosest(nums, target))
