import copy
class Solution:
    def findWords(self, board, words):
        rs = []
        for word in words:
            bu_bord = copy.deepcopy(board)
            if self.exist(bu_bord, word):
                rs.append(word)
        return rs

    def exist(self, board, word):
        flag = False

        def earch(i, j, mv_idx):
            nonlocal flag
            if mv_idx == len(word):
                flag = True
                return True
            cnd = []

            if i - 1 >= 0:
                if board[i - 1][j] != "READ":
                    cnd.append((i - 1, j))
            if i + 1 < len(board):
                if board[i + 1][j] != "READ":
                    cnd.append((i + 1, j))
            if j - 1 >= 0:
                if board[i][j - 1] != "READ":
                    cnd.append((i, j - 1))
            if j + 1 < len(board[0]):
                if board[i][j + 1] != "READ":
                    cnd.append((i, j + 1))

            for c in cnd:
                if board[c[0]][c[1]] == word[mv_idx]:
                    board[c[0]][c[1]] = "READ"
                    rs = earch(c[0], c[1], mv_idx + 1)
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

s = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
board = [["a","b"],["c","d"]]
words = ["abcb"]
print(s.findWords(board, words))