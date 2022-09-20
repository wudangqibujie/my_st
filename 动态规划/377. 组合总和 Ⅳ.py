class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [1 for _ in range(target + 1)]
        nums = sorted(nums)
        for ix in range(1, len(dp)):
            val = 0
            jx = 0
            # print("find", ix, nums[jx])
            while jx < len(nums) and ix >= nums[jx]:
                # print("B", ix - nums[jx], dp, ((ix - nums[jx]) in nums or (ix - nums[jx]) == 0))
                add_val = dp[ix - nums[jx]]
                # print(add_val)
                val += add_val
                jx += 1
            # print(ix, val)
            dp[ix] = val
        # print(dp)
        return dp[-1]


s = Solution()
nums = [1,2,3]
target = 4
# nums = [1, 2]
# target = 10

print(s.combinationSum4(nums, target))
print(2 ** 31)

