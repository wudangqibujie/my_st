class Solution:
    def countSubIslands(self, grid1, grid2):


        def search(i, j):
            # print("START", i, j)
            if i < 0 or i >= len(grid1):
                return True

            if j < 0 or j >= len(grid1[0]):
                return True

            if grid2[i][j] == 0:
                return True

            grid2[i][j] = 0
            rst = []
            for nx in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                nx_i, nx_j = nx
                rs = search(nx_i, nx_j)
                rst.append(rs)
            # print(i, j, rst, sum(rst))
            if grid1[i][j] == 0:
                return False
            if sum(rst) == 4:
                return True
            return False


        cnt = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    a = search(i, j)
                    # print(i, j, a)
                    if a:
                        cnt += 1
        return cnt


grid1 = [[1,1,1,0,0],
         [0,1,1,1,1],
         [0,0,0,0,0],
         [1,0,0,0,0],
         [1,1,0,1,1]]

grid2 = [[1,1,1,1,0],
         [0,0,1,1,1],
         [0,1,0,0,0],
         [1,1,1,1,0],
         [0,1,0,1,0]]
s = Solution()
rs = s.countSubIslands(grid1, grid2)
print(rs)

