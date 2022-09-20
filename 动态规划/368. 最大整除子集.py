class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        dp = [1 for _ in range(len(nums))]
        dp_rs = [[nums[0]]] + [[] for _ in range(len(nums) - 1)]
        # print(dp_rs)
        for i in range(1, len(nums)):
            j = i - 1
            can_ix = None
            while j >= 0:
                if nums[i] % nums[j] == 0:
                    if can_ix is None:
                        can_ix = j
                        continue
                    if dp[j] > dp[can_ix]:
                        can_ix = j
                j -= 1
            if can_ix is None:
                dp[i] = 1
                dp_rs[i] = [nums[i]]
                continue
            dp[i] = dp[can_ix] + 1
            dp_rs[i] = dp_rs[can_ix] + [nums[i]]
        ix = 0
        rs = 0
        print(nums)
        print(dp)
        print(dp_rs)
        while ix < len(dp):
            if dp[ix] > dp[rs]:
                rs = ix
            ix += 1
        print(ix)
        ix = rs if rs < len(dp) else rs - 1
        return dp_rs[ix]


s = Solution()
nums = [1,2,3]
# nums = [1, 2, 3, 4, 6, 8]
nums = [1,2,4,8]
nums = [1, 4, 8, 36]
nums = [3,4,16,8]
# nums = [4,8,10,240]
nums = [2,3,4,9,8]
print(s.largestDivisibleSubset(nums))