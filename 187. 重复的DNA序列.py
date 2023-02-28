class Solution:
    def findRepeatedDnaSequences(self, s):
        # print(len(s))
        rslt = []
        log = dict()
        for ix in range(10, len(s) + 1):
            c_str = s[ix - 10: ix]
            # print(c_str)
            if c_str in log:
                log[c_str] += 1
                continue
            log[c_str] = 1
        # print(log)
        for k, v in log.items():
            if v > 1:
                rslt.append(k)
        return rslt


s = Solution()
ss = "AAAAAAAAAAAAA"
print(s.findRepeatedDnaSequences(ss))