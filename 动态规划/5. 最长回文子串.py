class Solution:
    def longestPalindrome(self, s):
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        # for i in range(len(s)):
        #     for j in range(len(s)):
        sj = 0
        fg = 0
        rs = ""
        for i in range(len(s)):
            dp[i][i] = 1
            fg = 1
            rs = s[i: i + 1]
        for j in range(1, len(s)):
            dp[j - 1][j] = 2 if s[j - 1] == s[j] else -1
            if dp[j - 1][j] != -1:
                fg = 2
                rs = s[j - 1: j + 1]
        for k in [2, 3]:
            st_j = k
            while st_j < len(s):
                st_i = st_j - k
                i, j = st_i, st_j
                # print("STTTT", st_i, st_j)
                while j < len(s) and i >= 0:
                    if dp[i + 1][j - 1] == -1:
                        break
                    # print(i, j, fg)
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:
                        dp[i][j] = -1
                    if dp[i][j] > fg:
                        fg = dp[i][j]
                        rs = s[i: j + 1]
                    # print(i, j)
                    i -= 1
                    j += 1
                st_j += 1

        # for i in dp:
        #     print(i)
        # print(fg)
        return rs

s = Solution()
ss = "aba"
ss = "babad"
# ss =  "cbbd"
# ss = "aba"
# ss = "aaaaa"
# ss = "aacabdkacaa"
# ss = "aaaa"
print(s.longestPalindrome(ss))