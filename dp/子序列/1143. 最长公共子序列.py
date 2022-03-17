class Solution:
    def longestCommonSubsequence(self, text1, text2):
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

        dp[0][0] = 1 if text1[0] == text2[0] else 0
        print(dp)
        for i in range(1, len(text1)):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, len(text2)):
            if text2[j] == text1[0]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )
        for i in dp:
            print(i)

        return dp[-1][-1]


s = Solution()
s1="ezupkr"
s2="ubmrapg"
print(s.longestCommonSubsequence(s1, s2))
