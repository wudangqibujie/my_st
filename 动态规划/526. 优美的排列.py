from copy import deepcopy
class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """

        def cal(set_, ix):
            if ix == n:
                if ix % set_[0] == 0 or set_[0] % ix == 0:
                    return 1
                return 0
            rslt = 0
            # print(set_, ix)
            for xx in range(len(set_)):
                # print(set_[xx])
                set_buff = deepcopy(set_)
                if set_[xx] % ix == 0 or ix % set_[xx] == 0:
                    set_buff.pop(xx)
                    rs = cal(set_buff, ix + 1)
                    rslt += rs
            return rslt
        # return cal([i for i in range(1, n + 1)], 1)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    continue
                if i % j == 0 or j % i == 0:
                    dp[i][j] = 1
        for i in dp:
            print(i)

s = Solution()
print(s.countArrangement(4), "rrrrrr")
