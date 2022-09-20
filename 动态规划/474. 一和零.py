class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        ix, jx = len(strs[0].replace("1", "")), len(strs[0].replace("0", ""))
        while ix < m + 1:
            while jx < n + 1:
                dp[ix][jx] = 1
                jx += 1
            jx = len(strs[0].replace("0", ""))
            ix += 1
        dpp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs))]
        dpp[0] = dp
        for t in range(1, len(strs)):
            num_0, num_1 = len(strs[t].replace("1", "")), len(strs[t].replace("0", ""))
            # print(strs[: t + 1], num_0, num_1)
            for i in range(m + 1):
                for j in range(n + 1):
                    # print(i, j, i - num_0, j - num_1)
                    if 0 <= i - num_0 < m + 1 and 0 <= j - num_1 < n + 1:
                        # print(dpp[t-1][i - num_0][j - num_1])
                        rs1 = dpp[t - 1][i - num_0][j - num_1] + 1
                    else:
                        rs1 = dpp[t - 1][i][j]
                    #     rs1 = dpp[t - 1][i][j] + 1
                    # rs1 = dpp[t - 1][i - num_0][j - num_1] + 1 if 0 <= i - num_0 < m + 1 and 0 <= j - num_1 < n + 1 else dpp[t - 1][i][j]
                    rs2 = dpp[t - 1][i][j]
                    # print(rs1, rs2, "rrrrsss")
                    dpp[t][i][j] = max(rs1, rs2)

            # for i in dpp[t]:
            #     print(i)
            # print("*****************")
            # return dpp[-1][-1][-1]
        return dpp[-1][-1][-1]

s = Solution()
# strs = ["10", "0001", "111001", "1", "0"]
# m = 5
# n = 3
strs = ["0"]
m = 2
n = 1
print(s.findMaxForm(strs, m, n))