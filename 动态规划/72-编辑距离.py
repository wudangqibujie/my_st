class Solution:
    def minDistance(self, word1, word2):

        def dp(i, j):
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1

            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)

            rs = min(dp(i, j - 1) + 1, dp(i - 1, j - 1) + 1, dp(i - 1, j) + 1)
            return rs
        return dp(len(word1) - 1, len(word2) - 1)


s = Solution()
word1 = "horse"
word2 = "ros"
print(s.minDistance(word1, word2))