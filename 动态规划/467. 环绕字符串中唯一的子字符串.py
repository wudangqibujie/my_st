class Solution:
    def findSubstringInWraproundString(self, p):
        dp = [1 for _ in range(len(p))]
        dp_map = dict()
        s = "zabcdefghijklmnopqrstuvwxyz"
        for i in range(1, len(s)):
            dp_map[s[i]] = 0
        map_target = dict()
        for i in range(1, len(s)):
            map_target[s[i]] = s[i - 1]
        dp_map[p[0]] = 1
        # print(map_target)
        for i in range(1, len(p)):
            target_s = map_target[p[i]]
            target_s = p[i - 1]
            # print(i, p[i], target_s, dp_map[target_s])
            # if dp_map[target_s]
            # print(i)
            if p[i - 1] == map_target[p[i]]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
            if dp[i] > dp_map[p[i]]:
                dp_map[p[i]] = dp[i]
        # print(dp)
        # for k, v in dp_map.items():
        #     if v == 0:
        #         continue
            # print(k, v)
        # print(sum(dp))
        return sum(dp_map.values())

s = Solution()
m = "cdefghefghijklmnopqrstuvwxmnijklmnopqrstuvbcdefghijklmnopqrstuvwabcddefghijklfghijklmabcdefghijklmnopqrstuvwxymnopqrstuvwxyz"
m = "zab"

print(len(m))
print(s.findSubstringInWraproundString(m))