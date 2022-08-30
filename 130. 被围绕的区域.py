class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        readed = set()

        def search(i, j):
            if i == -1 or i == len(board) or j == -1 or j == len(board[0]):
                return False
            if board[i][j] == "X":
                return True
            board[i][j] = "X"
            candi = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            flg = []
            for ix, iy in candi:
                if f"{ix}-{iy}" in readed:
                    continue
                rs = search(ix, iy)
                flg.append(rs)
            # print(board)
                readed.add(f"{i}-{j}")

            print(i, j, flg, sum(flg))

            if sum(flg) != 4:
                board[i][j] = "O"
                return False
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and f"{i}-{j}" not in readed:
                    search(i, j)
                    readed.add(f"{i}-{j}")
        # search(0, 0)
        for i in board:
            print(i)


s = Solution()
board = [
     ["X","O","X","X", "O"],
     ["X","X","O","X", "X"],
     ["X","O","X","O", "X"],
     ["O","X","X","X", "X"]
         ]
# board = [["X"]]
board = [["O","O","O"],
         ["O","O","O"],
         ["O","O","O"]
         ]
board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
s.solve(board)