class Solution:
    def numDecodings(self, s):
        if s.startswith("0"):
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        for i in range(len(s)):
            if i > 0 and s[i] == "0":
                if s[i - 1] == "0":
                    return 0
                if int(s[i - 1]) > 2:
                    return 0
                dp[i + 1] = dp[i - 1]
            if s[i] != "0":
                add = dp[i]
                # print(i, s[i-1:i+1], add)
                if i >= 1 and s[i - 1] != "0" and int(s[i - 1: i + 1]) < 27:
                    add += dp[i - 1]
                # print(add)
                dp[i + 1] = add
        print(dp)
        return dp[-1]


s = Solution()
a = "12"
print(s.numDecodings(a))


