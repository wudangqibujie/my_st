class Solution:
    def productExceptSelf(self, nums):
        f, b = [1 for _ in range(len(nums) + 1)], [1 for _ in range(len(nums) + 1)]
        for ix in range(1, len(nums) + 1):
            f[ix] = f[ix - 1] * nums[ix - 1]
        # f = f[1: ]
        num_r = list(reversed(nums))
        for ix in range(1, len(num_r) + 1):
            b[ix] = b[ix - 1] * num_r[ix - 1]
        b.reverse()
        # b = b[: -1]
        # print(f)
        # print(b)
        rslt = []
        for ix in range(len(nums)):
            rslt.append(f[ix] * b[ix + 1])
        return rslt




s = Solution()
nums = [1, -2, 3]
print(s.productExceptSelf(nums))
