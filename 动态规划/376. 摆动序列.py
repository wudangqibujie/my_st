class Solution:
    def wiggleMaxLength(self, nums):
        dp_up = [1 for _ in range(len(nums))]
        dp_low = [1 for _ in range(len(nums))]
        for ix in range(1, len(nums)):
            fnd_idx = ix
            while fnd_idx >= 0:
                if nums[ix] < nums[fnd_idx]:
                    dp_up[ix] = dp_low[fnd_idx] + 1
                    break
                fnd_idx -= 1
            if ix < 0:
                dp_low[ix] = 1
            fnd_idx = ix
            while fnd_idx >= 0:
                if nums[ix] > nums[fnd_idx]:
                    dp_low[ix] = dp_up[fnd_idx] + 1
                    break
                fnd_idx -= 1
            if ix < 0:
                dp_up[ix] = 1
        return max(max(dp_low), max(dp_up))


s = Solution()
nums = [1]
print(s.wiggleMaxLength(nums))