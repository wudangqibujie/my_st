class Solution:
    def numSquares(self, n):
        dp = [None] + [0 for _ in range(n)]
        map_ = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        map_.reverse()
        # print(map_)
        # print(dp)
        for ix in range(1, len(dp)):
            flg = float("inf")
            if ix in map_:
                dp[ix] = 1
            else:
                for i in map_:
                    if ix < i:
                        continue
                    flg = min(flg, 1 + dp[ix - i])
                dp[ix] = flg
        # print(dp)
        return dp[-1]


s = Solution()
print(s.numSquares(7))