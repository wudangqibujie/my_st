class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rslt = []
        map_ = dict()
        for n in nums:
            map_[n] = 1 if n not in map_ else map_[n] + 1
        for k, v in map_.items():
            if v == 1:
                rslt.append(k)
        return rslt


s = Solution()
nums = [1,2,1,3,2,5]
print(s.singleNumber(nums))