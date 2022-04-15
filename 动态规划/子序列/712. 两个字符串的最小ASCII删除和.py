class Solution:
    def minimumDeleteSum(self, s1, s2):
        dp = [[0 for i in range(len(s2))] for _ in range(len(s1))]

        dp[0][0] = 0 if s1[0] == s2[0] else ord(s1[0]) + ord(s2[0])

        flag = True if dp[0][0] == 0 else False
        for i in range(1, len(s1)):
            if s1[i] == s2[0]:
                if not flag:
                    dp[i][0] = dp[i - 1][0] - ord(s1[i])
                    flag = True
                else:
                    dp[i][0] = dp[i - 1][0] + ord(s1[i])
            else:
                dp[i][0] = dp[i - 1][0] + ord(s1[i])
        flag = True if dp[0][0] == 0 else False
        # print(flag)
        for j in range(1, len(s2)):
            if s2[j] == s1[0]:
                if not flag:
                    dp[0][j] = dp[0][j - 1] - ord(s2[j])
                    flag = True
                else:
                    dp[0][j] = dp[0][j - 1] + ord(s2[j])
            else:
                dp[0][j] = dp[0][j - 1] + ord(s2[j])

        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + ord(s1[i]) + ord(s2[j]),
                        dp[i - 1][j] + ord(s1[i]),
                        dp[i][j - 1] + ord(s2[j])
                    )

        # for i in 动态规划:
        #     print(i)
        return dp[-1][-1]




s = Solution()
s1 = "a"
s2 = "a"
# s1 = "abc"
# s2 = "abc"s1 = "delete", s2 = "leet"
print(s.minimumDeleteSum(s1, s2))
# print(ord("a"), ord("s"), ord("e"))