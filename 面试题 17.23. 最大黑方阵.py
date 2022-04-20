class Solution:
    def findSquare(self, matrix):
        up = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        low = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        left = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        right = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        flg = 0
        rs = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    up[i][j] = 0 if matrix[i][j] == 1 else 1
                else:
                    up[i][j] = 0 if matrix[i][j] == 1 else 1 + up[i - 1][j]
                if j == 0:
                    left[i][j] = 0 if matrix[i][j] == 1 else 1
                else:
                    left[i][j] = 0 if matrix[i][j] == 1 else 1 + left[i][j - 1]
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if i == len(matrix) - 1:
                    low[i][j] = 0 if matrix[i][j] == 1 else 1
                else:
                    low[i][j] = 0 if matrix[i][j] == 1 else 1 + low[i + 1][j]
                if j == len(matrix[0]) - 1:
                    right[i][j] = 0 if matrix[i][j] == 1 else 1
                else:
                    right[i][j] = 0 if matrix[i][j] == 1 else 1 + right[i][j + 1]
        print("up")
        for i in up:

            print(i)
        print("left")
        for i in left:

            print(i)
        # print("low")
        # for i in low:
        #     print(i)
        # print("right")
        # for i in right:
        #     print(i)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    board_rng = min(low[i][j], right[i][j])
                    print(i, j, board_rng)
                    if flg == 0:
                        flg = 1
                        rs = [i, j, 1]
                    for k in range(1, board_rng):
                        if matrix[i + k][j + k] == 1:
                            continue
                        nxt_board_range = min(up[i + k][j + k], left[i + k][j + k])
                        print("aaaa", nxt_board_range, i + k, j + k)
                        if board_rng >= nxt_board_range:
                            if min(nxt_board_range, board_rng, k) > flg:
                                flg = min(nxt_board_range, board_rng, k)
                                rs = [i, j, min(nxt_board_range, board_rng, k)]
        return rs





s = Solution()
a = [[1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
     [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
     [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
     [0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
     [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
     [1, 1, 1, 0, 1, 0, 0, 1, 1, 1]]
# a = [
#    [0,1,1],
#    [1,0,1],
#    [1,1,0]
# ]
# a = [
#    [1,0,1],
#    [0,0,1],
#    [0,0,1]
# ]
# a = [[1, 1, 1, 0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 1, 1, 0, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]]
a = [[1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
     [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
     [1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
     [0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
     [0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
     [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
     [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
     [1, 0, 0, 1, 0, 0, 0, 1, 1, 1]]
print(s.findSquare(a))

for i in a:
    print(i)

# [5,3,2]