class Solution:
    def findTargetSumWays(self, nums, target):
        cnt = 0
        def backwards(idx, cum_sum):
            nonlocal cnt
            if idx == len(nums):
                if cum_sum == target:
                    cnt += 1
                return
            for can in [nums[idx], -nums[idx]]:
                cum_sum += can
                backwards(idx + 1, cum_sum)
                cum_sum -= can

        backwards(0, 0)
        return cnt

s = Solution()
a = [1, 0]
print(s.findTargetSumWays(a, 1))
