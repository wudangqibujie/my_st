class Solution:
    def isMatch(self, s, p):
        dp = [[0 for _ in range(len(p) + 1)] for _  in range(len(s) + 1)]
        dp[0][0] = 1
        for j in range(2, len(p) + 1, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == "*"
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j - 1] == "*":
                        if s[i - 1] == p[j - 2] or p[j - 2] == ".":
                            dp[i][j] = int(any([
                                dp[i][j - 2],   # *
                                dp[i - 1][j - 2],
                                dp[i - 1][j]
                            ]))
                        else:
                            dp[i][j] = dp[i][j - 2]
        for i in dp:
            print(i)
        return bool(dp[-1][-1])


so = Solution()
s = "a"
p = "."
print(so.isMatch(s, p))




