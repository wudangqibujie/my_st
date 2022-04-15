class Solution:
    def beautifulArray(self, n):
        rs = [0 for _ in range(n)]
        if n % 2 != 0:
            rs[-1] = n // 2 + 1
        if n % 2 != 0:
            i, j = n // 2 - 1, n // 2 + 1
            mv_i, mv_j = 0, n - 2
        else:
            i, j = n // 2 - 1, n // 2
            mv_i, mv_j = 0, n - 1
        # print(i, j, mv_i, mv_j)
        # print(rs)
        flg = 0
        while i >= 0:
            if flg % 2 == 0:
                rs[mv_i], rs[mv_j] = i + 1, j + 1
            else:
                rs[mv_i], rs[mv_j] = j + 1, i + 1
            flg += 1
            mv_i += 1
            mv_j -= 1
            i -= 1
            j += 1
        return rs

s = Solution()
print(s.beautifulArray(5))
# [3,1,2,5,4]


