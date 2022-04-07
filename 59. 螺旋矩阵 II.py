class Solution:
    def generateMatrix(self, n):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        iix, jjx = 0, 0
        readed = set()
        ix = iix
        jx = jjx
        flag = 1
        while f"{ix}_{jx}" not in readed and ix >= 0 and jx >= 0 and ix < len(matrix) and jx < len(matrix[0]):
            while jx < len(matrix[0]) and ix < len(matrix) and f"{ix}_{jx}" not in readed:
                readed.add(f"{ix}_{jx}")
                matrix[ix][jx] = flag
                flag += 1
                jx += 1
            jx -= 1
            ix += 1
            while ix < len(matrix) and f"{ix}_{jx}" not in readed:
                readed.add(f"{ix}_{jx}")
                matrix[ix][jx] = flag
                flag += 1
                ix += 1
            jx -= 1
            ix -= 1
            while jx >= 0 and ix < len(matrix) and f"{ix}_{jx}" not in readed:
                readed.add(f"{ix}_{jx}")
                matrix[ix][jx] = flag
                flag += 1
                jx -= 1
            ix -= 1
            jx += 1
            while jx >= 0 and ix < len(matrix) and ix >= 0 and f"{ix}_{jx}" not in readed:
                readed.add(f"{ix}_{jx}")
                matrix[ix][jx] = flag
                flag += 1
                ix -= 1
            iix += 1
            jjx += 1
            ix = iix
            jx = jjx
        return matrix


s = Solution()
a = s.generateMatrix(0)
for i in a:
    print(i)
