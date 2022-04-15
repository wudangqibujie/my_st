class Solution:
    def generateParenthesis(self, n):
        dp = [""]
        dp_num = [0]
        for _ in range(2*n):
            buff_dp = []
            buff_dp_num = []
            for ix in range(len(dp)):
                balance = dp_num[ix]
                buff_dp.append(dp[ix] + "(")
                buff_dp_num.append(balance + 1)
                if balance - 1 >= 0:
                    buff_dp.append(dp[ix] + ")")
                    buff_dp_num.append(balance - 1)
            dp = buff_dp
            # print(动态规划)
            dp_num = buff_dp_num
        res = []
        for ix in range(len(dp_num)):
            if dp_num[ix] == 0:
                res.append(dp[ix])
        return res


s = Solution()
print(s.generateParenthesis(4))





