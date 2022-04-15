class Solution:
    def longestPalindromeSubseq(self, s):

        def search(i, j):
            while (i >= 0 and j < len(s) and s[i] == s[j]):
                i -= 1
                j += 1
            return s[i + 1: j - i - 1]

        rs = ""
        for i in range(len(s)):
            r1 = search(i, i)
            r2 = search(i, i + 1)
            print(r1, r2)
            rs = r1 if len(r1) > len(rs) else rs
            rs = r2 if len(r2) > len(rs) else rs
        return rs


s = Solution()
a = "cbbd"
print(s.longestPalindromeSubseq(a))

