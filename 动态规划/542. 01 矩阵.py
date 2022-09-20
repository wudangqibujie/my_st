class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        dp = [[None for _ in range(len(mat[0]))] for _ in range(len(mat))]

        def search(i, j):



            # if not (0 <= i < len(mat) and 0 <= j < len(mat[0])):
            #     return "None"
            if mat[i][j] == 0:
                dp[i][j] = 0
                return 0
            # print(dp[i][j])
            # if dp[i][j] is not None:
            #     return dp[i][j]
            cand = [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
            cand = [i for i in cand if 0 <= i[0] < len(mat) and 0 <= i[1] < len(mat[0])]
            flg = False
            flg1 = False
            for ix, jx in cand:
                if mat[ix][jx] == 0:
                    flg = True
                if mat[ix][jx] == 1 and dp[ix][jx] is None:
                    flg1 = True
            print(i, j, flg, flg1, cand)
            if flg:
                dp[i][j] = 1
                return 1
            # if flg1:
            #     return
            rslt = []
            for ix, jx in cand:
                rs = search(ix, jx)
                if rs is None:
                    continue
                rslt.append(rs)
            dp[i][j] = min(rslt) + 1
            # print(rslt)
            return dp[i][j]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                search(i, j)
        for i in dp:
            print(i)


s = Solution()
mat = [[0,0,0],
       [0,1,0],
       [1, 1, 1],
       [1, 1, 1]]
s.updateMatrix(mat)


