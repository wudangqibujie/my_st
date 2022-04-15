class Solution:
    def replaceSpaces(self, S, length):
        s = ""
        ix = 0
        while ix < length:
            if ix == 0:
                if S[ix] == " ":
                    s = s + "%20"
                else:
                    s = s + S[ix]
            else:
                