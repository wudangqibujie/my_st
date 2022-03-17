class Solution:
    def longestPalindromeSubseq(self, s):

        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(len(s)):
                if i > j:
                    continue
                if i == j:
                    dp[i][j] = 1
                if j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 1

        st_i, st_j = 0, 2
        while st_j < len(s):

            xi, xj = st_i, st_j
            while xj < len(s):
                # print(xi, xj)
                if s[xi] == s[xj]:
                    dp[xi][xj] = dp[xi + 1][xj - 1] + 2
                else:
                    dp[xi][xj] = max(dp[xi][xj - 1], dp[xi + 1][xj])
                xi += 1
                xj += 1
            st_j += 1

        return dp[0][-1]


s = Solution()
a = "a"
print(s.longestPalindromeSubseq(a))