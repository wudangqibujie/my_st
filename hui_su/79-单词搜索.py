class Solution:
    def exist(self, board, word):
        flag = False
        def earch(i, j, mv_idx):
            nonlocal flag
            if mv_idx == len(word):
                flag = True
                return True
            cnd = []

            if i-1 >= 0 :
                if board[i - 1][j] != "READ":
                    cnd.append((i - 1, j))
            if i+1 < len(board):
                if board[i + 1][j] != "READ":
                    cnd.append((i + 1, j))
            if j-1 >= 0:
                if board[i][j - 1] != "READ":
                    cnd.append((i, j - 1))
            if j+1 < len(board[0]):
                if board[i][j + 1] != "READ":
                    cnd.append((i, j + 1))

            for c in cnd:
                if board[c[0]][c[1]] == word[mv_idx]:
                    board[c[0]][c[1]] = "READ"
                    rs = earch(c[0], c[1], mv_idx+1)
                    if rs:
                        return rs
                    board[c[0]][c[1]] = word[mv_idx]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = "READ"
                    r = earch(i, j, 1)
                    board[i][j] = word[0]
                    if r:
                        return r
        return False






board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
# print(len(word))
s = Solution()
print(s.exist(board, word))
# print(len(word))


