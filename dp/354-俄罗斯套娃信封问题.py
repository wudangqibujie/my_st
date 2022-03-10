class Solution:
    def maxEnvelopes(self, envelopes):
        sor1 = sorted(envelopes, key=lambda item: item[0])
        rs = [[sor1[0]]]
        idx = 1
        while idx < len(envelopes):
            lst_block = rs[-1]
            lst_block_key = lst_block[-1][0]
            nw_key = sor1[idx][0]
            if lst_block_key == nw_key:
                rs[-1].append(sor1[idx])
            else:
                rs.append([sor1[idx]])
            idx += 1
        new_rs = []
        for idx in range(len(rs)):
            a = sorted(rs[idx], key=lambda item: item[1], reverse=True)
            new_rs.extend(a)
        # print(new_rs)
        new_rs = [i[1] for i in new_rs]
        dp = [0 for _ in range(len(new_rs))]
        print(new_rs)
        dp[0] = 1
        for i in range(1, len(dp)):
            val = float("-inf")
            st = i - 1
            while st >= 0:
                if new_rs[st] < new_rs[i]:
                    if dp[st] > val:
                        val = dp[st]
                st -= 1
            dp[i] = val + 1 if val != float("-inf") else 0
        print(dp)
        return max(dp)




s = Solution()
# envelopes = [[1, 1], [4, 6], [4, 6], [2, 3], [6, 3], [6, 6]]
envelopes = [[46,89],[50,53],[52,68],[72,45],[77,81]]
print(s.maxEnvelopes(envelopes))
