class Solution:
    def numEnclaves(self, grid):

        def search(i, j):
            if i < 0 or i >= len(grid):
                return 1, 0
            if j < 0 or j >= len(grid[0]):
                return 1, 0
            if grid[i][j] == 0:
                return 0, 0
            grid[i][j] = 0
            rs = []
            b = 0
            for nxt in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                nxt_i, nxt_j = nxt
                buff_rs, flag = search(nxt_i, nxt_j)
                rs.append(buff_rs)
                b += flag
            if sum(rs) == 0:
                return 0, b + 1
            return 1, b + 0

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # print(i, j)
                    rs, buff_cnt = search(i, j)
                    # print(buff_cnt)
                    if rs == 0:
                        cnt += buff_cnt
        return cnt


s = Solution()
m = [[0,0,0,0],
     [0,0,1,0],
     [0,0,0,0],
     [1,1,1,0],
     [0,0,0,0],
     [0,1,1,0],
     [0,0,0,0]]
print(s.numEnclaves(m))