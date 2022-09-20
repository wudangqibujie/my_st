class Solution:
    def reverseVowels(self, s):
        yy = ["a", "e", "i", "o", "u"]
        yy += [i.upper() for i in yy]
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in yy:
                i += 1
            while i< j and s[j] not in yy:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)


s = Solution()
ss = "afaA"
print(s.reverseVowels(ss))
