class Solution:
    def largestRectangleArea(self, heights):
        left = [0 for _ in range(len(heights))]
        right = [0 for _ in range(len(heights))]

        # left[0] = -1

        ix = 1
        stack = [(heights[0], 0)]
        while ix < len(heights) + 1:
            if ix == len(heights):
                while stack:
                    _, pop_ix = stack.pop()
                    right[pop_ix] = len(heights)
                break
            while stack and heights[ix] < stack[-1][0]:
                _, pop_ix = stack.pop()
                right[pop_ix] = ix
            stack.append((heights[ix], ix))
            ix += 1


        ix = len(heights) - 2
        stack = [(heights[-1], len(heights) - 1)]
        while ix >= -1:
            if ix == -1:
                while stack:
                    _, pop_ix = stack.pop()
                    left[pop_ix] = ix
                break
            while stack and heights[ix] < stack[-1][0]:
                _, pop_ix = stack.pop()
                left[pop_ix] = ix
            stack.append((heights[ix], ix))
            ix -= 1
        rs = 0
        d = []
        for i in range(len(heights)):
            val = (right[i] - left[i] - 1) * heights[i]
            rs = max(rs, val)
            d.append(rs)
        # print(right)
        # print(left)
        # print(heights)
        # print(d)
        return rs




s = Solution()
heights = [1, 1, 4, 4, 4]
print(s.largestRectangleArea(heights))
