class Solution:
    def isValidSudoku(self, board):
        rs = True
        for i in range(9):
            readed = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in readed:
                    return False
                readed.add(board[i][j])
            if not rs:
                return False
        for j in range(9):
            readed = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in readed:
                    return False
                readed.add(board[i][j])
            if not rs:
                return False


        for ix in range(0, 9, 3):
            for jx in range(0, 9, 3):
                readed = set()
                for i in range(ix, ix + 3):
                    for j in range(jx, jx + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in readed:
                            # print("2", i, j)

                            return False
                        readed.add(board[i][j])
                if not rs:
                    return False
        return True


s = Solution()
board = [[".",".","4",".",".",".","6","3","."],
         [".",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".","9","."],
         [".",".",".","5","6",".",".",".","."],
         ["4",".","3",".",".",".",".",".","1"],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]



print(s.isValidSudoku(board))

