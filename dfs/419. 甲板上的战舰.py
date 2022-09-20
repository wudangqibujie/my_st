class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        dp = [[None for _ in range(len(board[0]))] for _ in range(len(board))]

        def search(i, j):
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])):
                return
            if dp[i][j] or board[i][j] == ".":
                return
            dp[i][j] = True
            search(i - 1, j)
            search(i + 1, j)
            search(i, j - 1)
            search(i, j + 1)
        cnt = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X" and dp[i][j] is None:
                    search(i, j)
                    cnt += 1
        return cnt


s = Solution()
board = [["X","X","X","X"],]
print(s.countBattleships(board))
