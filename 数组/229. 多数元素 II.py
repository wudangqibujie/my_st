class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        map_ = dict()
        for i in nums:
            if i in map_:
                map_[i] += 1
            else:
                map_[i] = 1
        gap = len(nums) // 3
        rslt = []
        # print(map_)
        for k, v in map_.items():
            if v > gap:
                rslt.append(k)
        return rslt


s = Solution()
nums = [3,2,3]
# nums = [1]
nums = [1,2]
print(s.majorityElement(nums))