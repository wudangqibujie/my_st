class Solution:
    def isInterleave(self, s1, s2, s3):
        if (len(s1) == 0 and len(s2) == 0 and len(s3) != 0) or (len(s1) + len(s2)) != len(s3):
            return False
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = 0
        for i in range(1, len(s1) + 1):
            if s1[: i] == s3[: i]:
                dp[i][0] = i
            else:
                dp[i][0] = -1
        for j in range(1, len(s2) + 1):
            if s2[: j] == s3[: j]:
                dp[0][j] = j
            else:
                dp[0][j] = -1

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if dp[i - 1][j] == -1 and dp[i][j - 1] == -1:
                    dp[i][j] = -1
                    continue

                if dp[i - 1][j] != -1:
                    if s1[i - 1] == s3[dp[i - 1][j]]:
                        dp[i][j] = dp[i - 1][j] + 1
                        continue
                    else:
                        dp[i][j] = -1
                if dp[i][j - 1] != -1:
                    if s2[j - 1] == s3[dp[i][j - 1]]:
                        dp[i][j] = dp[i][j - 1] + 1
                        continue
                    else:
                        dp[i][j] = -1
        for i in dp:
            print(i)
        return dp[-1][-1] != -1


s = Solution()
s1 = "a"
s2 = ""
s3 = "aa"
print(s.isInterleave(s1, s2, s3))