class Solution:
    def minSubArrayLen(self, target, nums):
        rs = None
        cal = nums[0]
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            print(i, j, rs, cal)
            if i == j and i == len(nums) - 1:
                if rs is None:
                    return 0
                return rs
            if cal < target:
                if j != len(nums) - 1:
                    cal += nums[j]
                    j += 1
            else:
                cal -= nums[i]
                i += 1
                if rs is None:
                    rs = j - i + 1
                else:
                    rs = min(rs, j - i + 1)
s = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(s.minSubArrayLen(target, nums))