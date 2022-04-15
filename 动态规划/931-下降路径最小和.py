class Solution:
    def minFallingPathSum(self, matrix):
        dp = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
        dp[0] = matrix[0]
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                candi = []
                if j - 1 >= 0:
                    candi.append((i - 1, j - 1))
                if j + 1 < len(matrix[0]):
                    candi.append((i - 1, j + 1))
                candi.append((i - 1, j))
                can_vals = []
                # print(candi)
                for nx in candi:
                    # print(nx, "NX")
                    can_vals.append(dp[nx[0]][nx[1]])
                # print(can_vals)
                dp[i][j] = min(can_vals) + matrix[i][j]
        # print(动态规划)
        return min(dp[-1])


s = Solution()
matrix = [[-19,57],[-40,-5]]
print(s.minFallingPathSum(matrix))
