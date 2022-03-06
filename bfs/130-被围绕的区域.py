class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        def backward(i, j):
            # print("START", i, j)
            if i == -1 or i == len(board):
                return 1
            if j == -1 or j == len(board[0]):
                return 1
            if board[i][j] == "X":
                return 0
            cand_idxes = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            flag_rs = []
            board[i][j] = "X"
            for idx in cand_idxes:
                nxt_i, nxt_j = idx
                rs = backward(nxt_i, nxt_j)
                flag_rs.append(rs)
            print("结果", flag_rs, i, j)
            if sum(flag_rs) != 0:
                print(i, j)
                board[i][j] = "O"
                return 1
            return 0

        backward(1, 2)
        for k in board:
            print(k)
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] == "O":
        #             print(f"********{(i, j)}**********")
        #             backward(i, j)
        #             for k in board:
        #                 print(k)

s = Solution()
board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","O","X"]]
s.solve(board)

