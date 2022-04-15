class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums.sort()
        idx = 1
        print(nums)
        rs = 1
        while idx < len(nums):
            mv_idx = idx
            # print(idx, nums)
            cnt = 1
            while mv_idx < len(nums) and (nums[mv_idx] - nums[mv_idx - 1]) <= 1:
                if (nums[mv_idx] - nums[mv_idx - 1]) == 1:
                    cnt += 1
                mv_idx += 1

            rs = max(rs, cnt)
            idx = mv_idx + 1
        return rs


s = Solution()
nums = [1,2,0,1]
print(s.longestConsecutive(nums))





