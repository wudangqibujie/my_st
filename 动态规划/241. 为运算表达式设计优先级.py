class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        dp = dict()
        ch = ["+", "-", "*"]

        def cal(line):
            # print("line", line)
            if "+" not in line and "-" not in line and "*" not in line:
                # print(line)
                if line not in dp:
                    dp[line] = [int(line)]
                return [int(line)]
            rslt = []
            for ix, l in enumerate(line):
                if l not in ch:
                    continue
                l_ch = line[: ix]
                r_ch = line[ix + 1: ]
                # print(l_ch, l, r_ch)
                if l_ch in dp:
                    l_rs = dp[l_ch]
                else:
                    l_rs = cal(l_ch)
                if r_ch in dp:
                    r_rs = dp[r_ch]
                else:
                    r_rs = cal(r_ch)
                for k in l_rs:
                    for j in r_rs:
                        rslt.append(eval(f"{k}{l}{j}"))
            dp[line] = rslt
            return rslt

        return cal(expression)


s = Solution()
expression = "2"
print(s.diffWaysToCompute(expression))
