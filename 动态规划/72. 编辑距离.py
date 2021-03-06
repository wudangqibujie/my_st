class Solution:
    def minDistance(self, word1, word2):
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for j in range(1, len(word2) + 1):
            dp[0][j] = dp[0][j - 1] + 1

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i - 1][j - 1] + 1,
                        dp[i][j - 1] + 1
                    )
        # for i in 动态规划:
        #     print(i)
        return dp[-1][-1]

s = Solution()
word1 = "intention"
word2 = "execution"
print(s.minDistance(word1, word2))