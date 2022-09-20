class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def identify_1(i, j):
            cnt = 0
            candi = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1), (i + 1, j + 1)]
            for ix, jx in candi:
                if not (0 <= ix < len(board) and 0 <= jx < len(board[0])):
                    continue
                if board[ix][jx] == 1:
                    cnt += 1
            return int(cnt in (2, 3))

        def identify_0(i, j):
            cnt = 0
            candi = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1), (i + 1, j + 1)]
            for ix, jx in candi:
                if not (0 <= ix < len(board) and 0 <= jx < len(board[0])):
                    continue
                if board[ix][jx] == 1:
                    cnt += 1
            # print(i, j, cnt)
            return int(cnt == 3)

        rslt = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                rslt[i][j] = identify_1(i, j) if board[i][j] == 1 else identify_0(i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = rslt[i][j]



s = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# board = [[1,1],[1,0]]
# board = [[1]]
print(s.gameOfLife(board))


