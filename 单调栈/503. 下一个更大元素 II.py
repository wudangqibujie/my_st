class Solution:
    def nextGreaterElements(self, nums):
        rs = [None for _ in range(len(nums))]
        stack = []
        idx = 0
        while idx < 2 * len(nums):
            while stack and nums[idx % len(nums)] > stack[-1][0]:
                pop_val, pop_idx = stack.pop()
                # if rs[idx % len(nums)] is None:
                rs[pop_idx % len(nums)] = nums[idx % len(nums)]

            stack.append([nums[idx % len(nums)], idx])
            idx += 1
        # print(rs)
        for i in range(len(rs)):
            if rs[i] is None:
                rs[i] = -1
        print(rs)
        return rs

nums = [1,2,3,2,1]
s = Solution()
s.nextGreaterElements(nums)