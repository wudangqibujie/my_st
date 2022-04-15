class Solution:
    def multiply(self, num1, num2):
        flag = 1
        ix = len(num1) - 1
        buff = "0"
        while ix >= 0:
            jx = len(num2) - 1
            while jx >= 0:
                vl = int(num1[ix]) * int(num2[jx])





    def addStrings(self, num1, num2):
        i, j = len(num1), len(num2)
        add = 0
        rs = ""
        while (i >= 0 or j >= 0):
            i = i - 1 if i >= 0 else i
            j = j - 1 if j >= 0 else j
            a_vl = int(num1[i]) if i >= 0 else 0
            b_vl = int(num2[j]) if j >= 0 else 0
            if i < 0 and j < 0:
                if add == 1:
                    rs = "1" + rs
                break
            vl_bu = a_vl + b_vl + add
            rs = str(vl_bu % 10) + rs
            add = 1 if vl_bu >= 10 else 0
        return rs