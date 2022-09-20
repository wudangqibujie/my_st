class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.cal_cum_sum()


    def cal_cum_sum(self):
        col_cum = [[0 for _ in range(len(self.matrix[0]) + 1)] for _ in range(len(self.matrix) + 1)]
        row_cum = [[0 for _ in range(len(self.matrix[0]) + 1)] for _ in range(len(self.matrix) + 1)]
        slant_cum = [[0 for _ in range(len(self.matrix[0]) + 1)] for _ in range(len(self.matrix) + 1)]
        for j in range(1, len(col_cum[0])):
            for i in range(1, len(col_cum)):
                col_cum[i][j] = col_cum[i - 1][j] + self.matrix[i - 1][j - 1]
        for i in range(1, len(col_cum)):
            for j in range(1, len(col_cum[0])):
                row_cum[i][j] = row_cum[i][j - 1] + self.matrix[i - 1][j - 1]
        for i in range(1, len(col_cum)):
            for j in range(1, len(col_cum[0])):
                slant_cum[i][j] = slant_cum[i - 1][j - 1] + col_cum[i - 1][j] + row_cum[i][j - 1] + self.matrix[i - 1][j - 1]
        self.col_cum = col_cum
        self.row_cum = row_cum
        self.slant_cum = slant_cum
        # for i in col_cum:
        #     print(i)
        # print()
        # for i in row_cum:
        #     print(i)
        print()
        for i in slant_cum:
            print(i)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        rslt = self.slant_cum[row2 + 1][col2 + 1] - self.slant_cum[row1][col2 + 1] - self.slant_cum[row2 + 1][   col1] + self.slant_cum[row1][col1]
        print(self.slant_cum[row2 + 1][col2 + 1] , self.slant_cum[row1][col2 + 1] , self.slant_cum[row2 + 1][col1] , self.slant_cum[row1][col1])
        return rslt




m = [[1],
      [-7]]
s = NumMatrix(m)
row1, col1, row2, col2 = [1,0,1,0]
print(s.sumRegion(row1, col1, row2, col2))



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
# [[[[1],[-7]]],[0,0,0,0],[1,0,1,0],[0,0,1,0]]