class Solution:
    def addBinary(self, a, b):
        i, j = len(a) - 1, len(b) - 1
        add = 0
        rs = ""
        while True:
            aa, bb = a[i], b[j]
            if aa == "0" and bb == "0":
                rs = 0
            if aa == "0" and bb == "1":
                rs = 1
            if aa == "1" and bb == "0":
                rs = 1
            if aa == "1" and bb == "1":
                rs = 0
                add = 0
            


