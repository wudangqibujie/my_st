class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        Fn_1 = sum([i * nums[i] for i in range(len(nums))])
        rs = Fn_1
        length = len(nums)
        # print(Fn_1)
        nums = nums + nums
        # print(nums)
        tree_sum = [0]
        for i in nums:
            tree_sum.append(tree_sum[-1] + i)
        tree_sum = tree_sum[1: ]
        for sp in range(length, len(nums) - 1):
            # print(Fn_1, nums[sp], (length - 1), (tree_sum[sp - 1], tree_sum[sp - length]))
            Fn = Fn_1 + nums[sp] * (length - 1) - (tree_sum[sp - 1] - tree_sum[sp - length])
            rs = Fn if Fn > rs else rs
            Fn_1 = Fn
        return rs


nums = [4,3,2,6]
# nums = [100]
s = Solution()
print(s.maxRotateFunction(nums))