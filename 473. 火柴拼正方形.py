class Solution:
    def makesquare(self, matchsticks):
        matchsticks.sort()
        tnt = sum(matchsticks)
        print(matchsticks, tnt)
        board_len = tnt // 4
        print(board_len)


s = Solution()
M = [3,3,3,3,4]
s.makesquare(M)