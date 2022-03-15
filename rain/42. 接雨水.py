class Solution:
    def trap(self, height):
        stack = []
        rs_idx = [None for _ in range(len(height))]
        rs_val = [None for _ in range(len(height))]
        ix = 0
        while ix < len(height):
            i = height[ix]
            while stack and stack[-1][-1] <= i:
                pop_idx, pop_val = stack.pop()
                # rs.append([pop_idx, pop_val, ix, i])  # 此时idx，此时值， 下一个大于自己的idx, 下一个大于自己的值
                rs_idx[pop_idx] = ix
                rs_val[pop_idx] = i
            stack.append((ix, i))
            ix += 1
            if ix == len(height):
                while stack:
                    pop_idx, pop_val = stack.pop()
                    # rs.append([pop_idx, pop_val, -1, -1])
                    rs_idx[pop_idx] = -1
                    rs_val[pop_idx] = -1
        # print(height, "源")
        # print(rs_idx, "IDX")
        # print(rs_val, "VAL")
        cnt = 0
        readed = [False for _ in range(len(height))]

        for ix in range(len(height)):
            if height[ix] == 0 or rs_idx[ix] == -1:
                continue
            if readed[ix]:
                cnt -= height[ix]
            else:
                cnt += (rs_idx[ix] - ix - 1) * min(height[ix], rs_val[ix])
                for j in range(ix, rs_idx[ix]):
                    readed[j] = True
        # print(cnt)
        return cnt

s = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(height))