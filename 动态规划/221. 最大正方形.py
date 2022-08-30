class Solution:
    def maximalSquare(self, matrix):
        dp_left = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        dp_up = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        rs = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    dp_left[i][j] = 0
                    continue
                dp_left[i][j] = dp_left[i][j - 1] + 1 if j > 0 else 1
                dp_up[i][j] = dp_up[i - 1][j] + 1 if i > 0 else 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # print(i, j)
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                    rs = max(rs, dp[i][j] ** 2)
                    continue
                if matrix[i][j] == "1":
                    if dp[i - 1][j - 1] != 0:
                        # if dp_up[i][j] >= dp[i - 1][j - 1] + 1 and dp_left[i][j] >= dp[i - 1][j - 1] + 1:
                        dp[i][j] = min(dp[i - 1][j - 1] + 1, dp_left[i][j], dp_up[i][j])
                        # else:
                        #     dp[i][j] = 1
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = 0
                # print(dp[i][j] ** 2, dp[i][j])
                rs = max(rs, dp[i][j] ** 2)

        # for i in dp_left:
        #     print(i)
        # print()
        # for i in dp_up:
        #     print(i)
        # print()
        # for i in dp:
        #     print(i)
        return rs

s = Solution()
matrix = [["0","0","0","1"],
          ["1","1","0","1"],
          ["1","1","1","1"],
          ["0","1","1","1"],
          ["0","1","1","1"]]
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
print(s.maximalSquare(matrix))
