class Solution:
    def lengthOfLastWord(self, s):
        ix = len(s)-1
        rs = 0
        if len(s) == 0:
            return rs
        while 1:
            if (s[ix] == " " or ix < 0) and rs != 0:
                return rs
            if s[ix] != " ":
                rs += 1
            ix -= 1
        # return 0

s = Solution()
a = "            aas     asd   a"
print(s.lengthOfLastWord(a))





