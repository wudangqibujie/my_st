class Solution:
    def findDisappearedNumbers(self, nums):
        ix = 0
        rs = []
        while ix < len(nums):
            if nums[ix] is None or nums[ix] - 1 == ix:
                ix += 1
                continue
            if nums[nums[ix] - 1] != nums[ix]:
                tmp = nums[ix]
                nums[ix] = nums[nums[ix] - 1]
                nums[tmp - 1] = tmp
            else:
                rs.append(ix + 1)
                nums[ix] = None
        return rs




s = Solution()
nums = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(nums))