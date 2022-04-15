class Solution:
    def closedIsland(self, grid):

        def search(i, j):
            if i < 0 or i >= len(grid):
                return 1
            if j < 0 or j >= len(grid[0]):
                return 1
            if grid[i][j] == 1:
                return 0
            rs = []
            grid[i][j] = 1
            for nxt in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                nxt_i, nxt_j = nxt
                rs.append(search(nxt_i, nxt_j))
            if sum(rs) == 0:
                return 0
            return 1

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and  search(i, j) == 0:
                    res += 1
                    # print(grid, i, j)
        return res



s = Solution()

a = [[1,1,1,1,1,1,1,0],
     [0,1,0,1,0,1,1,0],
     [1,0,1,1,1,1,1,0],
     # [1,0,0,0,0,1,1,1],
     # [1,1,1,1,1,1,1,0]
     ]


print(s.closedIsland(a))
