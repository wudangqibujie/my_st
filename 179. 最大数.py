class Solution:
    def largestNumber(self, nums):
        nums = [str(i) for i in nums]
        map_ = dict()
        for i in range(len(nums)):
            if nums[i][0] not in map_:
                map_[nums[i][0]] = [nums[i]]
            else:
                map_[nums[i][0]].append(nums[i])
        s = ''
        print(map_)
        # for k in range(9, 0, -1):
        #     if str(k) in map_:



s = Solution()
nums = [3,30,34,5,9]
print(s.largestNumber(nums))

