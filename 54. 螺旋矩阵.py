class Solution:
    def spiralOrder(self, matrix):
        iix, jjx = 0, 0
        readed = set()
        rs = []
        ix = iix
        jx = jjx
        while f"{ix}_{jx}" not in readed and ix >= 0 and jx >= 0 and ix < len(matrix) and jx < len(matrix[0]):
            while jx < len(matrix[0]) and ix < len(matrix) and f"{ix}_{jx}" not in readed:
                # print(ix, jx)
                readed.add(f"{ix}_{jx}")

                rs.append(matrix[ix][jx])
                jx += 1
                # print(jx)
            # print("A")
            # print(rs)
            jx -= 1
            ix += 1
            while ix < len(matrix) and f"{ix}_{jx}" not in readed:
                # print(ix, jx)
                readed.add(f"{ix}_{jx}")
                rs.append(matrix[ix][jx])
                ix += 1

            # print("B")
            # print(rs)
            jx -= 1
            ix -= 1
            while jx >= 0 and ix < len(matrix) and f"{ix}_{jx}" not in readed:
                # print(ix, jx)
                readed.add(f"{ix}_{jx}")
                rs.append(matrix[ix][jx])
                jx -= 1
            ix -= 1
            jx += 1
            # print("C")
            # print(rs, ix, jx)
            while jx >= 0 and ix < len(matrix) and ix >= 0 and f"{ix}_{jx}" not in readed:
                # print(ix, jx)
                readed.add(f"{ix}_{jx}")
                rs.append(matrix[ix][jx])
                ix -= 1
            # print("D")
            # print(rs)
            # print(readed)
            iix += 1
            jjx += 1
            ix = iix
            jx = jjx
            # print(ix, jx)
        return rs


s = Solution()
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
print(s.spiralOrder(matrix))
# [1,2,3,6,9,8,7,4,5]