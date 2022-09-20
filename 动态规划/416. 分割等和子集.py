from copy import deepcopy
class Solution:
    def canPartition(self, nums):
        target = sum(nums)
        if target % 2 != 0 or len(nums) == 1 or max(nums) > target // 2:
            return False
        target //= 2
        nums = sorted(nums)
        # print(nums)
        dp = [[0 for _ in range(len(nums))] for _ in range(target + 1)]
        dp[0] = [1 for _ in range(len(nums))]
        dp[nums[0]][0] = 1
        # for d in dp:
        #     print(d)
        for ix in range(1, target + 1):
            for jx in range(1, len(nums)):
                # print(ix - nums[jx], jx)
                if ix - nums[jx] < 0:
                    dp[ix][jx] = dp[ix][jx - 1]
                    continue
                dp[ix][jx] = max(dp[ix - nums[jx]][jx - 1], dp[ix][jx - 1])
        # for d in dp:
        #     print(d)
        return bool(dp[-1][-1])

nums = [1,5,11,5]
# nums = [1, 3, 2, 5]
nums = [6, 3, 3]
nums = [2]
s = Solution()
print(s.canPartition(nums))