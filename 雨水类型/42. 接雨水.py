class Solution:
    def trap(self, height):
        l_max = [0 for _ in range(len(height))]
        r_max = [0 for _ in range(len(height))]
        l_max[0] = height[0]
        for i in range(1, len(height)):
            if l_max[i - 1] <= height[i]:
                l_max[i] = height[i]
            else:
                l_max[i] = l_max[i - 1]
        r_max[-1] = height[-1]
        ix = len(height) - 2
        while ix >= 0:
            if r_max[ix + 1] <= height[ix]:
                r_max[ix] = height[ix]
            else:
                r_max[ix] = r_max[ix + 1]
            ix -= 1
        # print(l_max)
        # print(r_max)
        cnt = 0
        for i in range(1, len(height) - 1):
            cnt += min(l_max[i], r_max[i]) - height[i]
        return cnt




s = Solution()
height = [4,2,3]
print(s.trap(height))
