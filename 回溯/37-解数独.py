import copy
class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        def get_valid(i, j):
            blk_i, blk_j = i // 3, j // 3
            invald_set = set()
            for sc_j in range(9):
                if board[i][sc_j] == ".":
                    continue
                invald_set.add(board[i][sc_j])
            for sc_i in range(9):
                if board[sc_i][j] == ".":
                    continue
                invald_set.add(board[sc_i][j])
            for blk_ix in range(3 * blk_i, blk_i * 3 + 3):
                for blk_jx in range(3 * blk_j, blk_j * 3 + 3):
                    if board[blk_ix][blk_jx] == ".":
                        continue
                    invald_set.add(board[blk_ix][blk_jx])
            rs = []
            for csn in range(1, 10):
                if str(csn) not in invald_set:
                    rs.append(str(csn))
            return rs

        flag = 0
        def batckward(i, j):
            nonlocal flag
            nx_j = j + 1 if j < 8 else 0
            nx_i = i + 1 if j == 8 else i
            if i > 8:
                # print(m)
                # print(i, j, "scuess")
                # print(m)
                flag = 1
                return
            if board[i][j] == ".":
                valid_set = get_valid(i, j)
                # print(i, j, nx_i, nx_j)
                # print(i, j, valid_set)
                for valid in valid_set:
                    # print(i, j, nx_i, nx_j)
                    board[i][j] = str(valid)
                    batckward(nx_i, nx_j)
                    if flag == 1:
                        return
                    board[i][j] = "."
            else:
                batckward(nx_i, nx_j)
                if flag == 1:
                    return
        batckward(0, 0)

s = Solution()
m = [
['.', '2', '9', '.', '.', '.', '8', '.', '.'],
['.', '5', '3', '.', '.', '1', '.', '.', '2'],
['.', '7', '.', '2', '8', '.', '3', '.', '.'],
['.', '.', '.', '.', '.', '.', '7', '.', '.'],
['.', '.', '2', '6', '.', '3', '.', '.', '.'],
['.', '.', '.', '8', '.', '.', '.', '9', '.'],
['4', '.', '.', '.', '6', '.', '.', '.', '5'],
['9', '3', '.', '.', '.', '.', '.', '6', '.'],
['.', '.', '.', '3', '.', '5', '4', '8', '.'],
]


s.solveSudoku(m)
for i in m:
    print(i)
import numpy as np
r = []
for n in m:
    bu = [int(i) for i in n]
    r.append(bu)

rs = np.array(r)
print(rs.sum(axis=0))
print(rs.sum(axis=1))
for _ in range(9):
    print(str(["." for _ in range(9)])+",")