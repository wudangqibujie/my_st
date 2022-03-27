class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) - 1):
            for j in range(i, len(matrix[0])):
                print(i, j)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            jl, jr = 0, len(matrix[0]) - 1
            while jl < jr:
                matrix[i][jl], matrix[i][jr] = matrix[i][jr], matrix[i][jl]
                jl += 1
                jr -= 1




s = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(matrix)
