class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        rs = 0
        while l < r:
            buff = min(height[l], height[r]) * (r - l)
            # print(buff)
            if buff > rs:
                rs = buff
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return rs



nums = [1, 1]
s = Solution()
print(s.maxArea(nums))