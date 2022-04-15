class Solution:
    def minDistance(self, word1, word2):
        dp = [[0 for _ in range(len(word2))] for _ in range(len(word1))]
        dp[0][0] = 0 if word2[0] == word1[0] else 2
        # print(动态规划)
        flag = True if dp[0][0] == 0 else False
        for i in range(1, len(word1)):
            if word1[i] == word2[0]:
                if not flag:
                    dp[i][0] = dp[i - 1][0] - 1
                    flag = True
                else:
                    dp[i][0] = dp[i - 1][0] + 1
            else:
                dp[i][0] = dp[i - 1][0] + 1
        flag = True if dp[0][0] == 0 else False
        print(flag)
        for j in range(1, len(word2)):
            if word2[j] == word1[0]:
                if not flag:
                    dp[0][j] = dp[0][j - 1] - 1
                    flag = True
                else:
                    dp[0][j] = dp[0][j - 1] + 1
            else:
                dp[0][j] = dp[0][j - 1] + 1
        print(dp)
        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + 2,
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1
                    )

        for i in dp:
            print(i)
        return dp[-1][-1]


s = Solution()
word1 = "teacher"
word2 = "attacher"
# "teacher"
# "attacher"
print(s.minDistance(word1, word2))