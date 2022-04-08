class Solution:
    def maxProduct(self, words):
        matr = [[0 for _ in range(26)] for _ in range(len(words))]

        for ix, w in enumerate(words):
            for jx, i in enumerate(w):
                wo_idx = ord(i) - 97
                matr[ix][wo_idx] += 1
        for i in matr:
            print(i)
        val = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                rs1, rs2 = 0, 0
                for k in range(26):
                    flag = matr[i][k] ^ matr[j][k]
                    if flag == 0:
                        continue
                    if matr[i][k] != 0:
                        rs1 += matr[i][k]
                    else:
                        rs2 += matr[j][k]
                val = max(rs1 * rs2, val)
                # print(i, j, val, rs1, rs2)
        return val


# print(2 ^ 0)

s = Solution()
words = ["a","ab","ac"]
print(s.maxProduct(words))

