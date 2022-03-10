class Solution:
    def countSquares(self, matrix):
        dp_table_transpose = [[0 for _ in range(len(matrix[0]) + 1) ]for _ in range(len(matrix) + 1)]
        dp_table_move_upon = [[0 for _ in range(len(matrix[0]) + 1) ]for _ in range(len(matrix) + 1)]
        dp_table_move_right = [[0 for _ in range(len(matrix[0]) + 1) ]for _ in range(len(matrix) + 1)]
        st_i, st_j = len(matrix) - 1, len(matrix[0]) - 1
        while st_i >= 0:
            i, j = st_i, st_j
            while i >= 0 and j >= 0:
                if matrix[i][j] == 0:
                    dp_table_transpose[i][j] = 0
                else:
                    dp_table_transpose[i][j] = dp_table_transpose[i + 1][j + 1] + 1
                i -= 1
                j -= 1
            i, j = st_i, st_j
            while j >= 0:
                if matrix[i][j] == 0:
                    dp_table_move_right[i][j] = 0
                else:
                    dp_table_move_right[i][j] = dp_table_move_right[i][j + 1] + 1
                j -= 1
            st_i -= 1
        st_i, st_j = len(matrix) - 1, len(matrix[0]) - 1
        while st_j >= 0:
            i, j = st_i, st_j
            while i >= 0 and j >= 0:
                if matrix[i][j] == 0:
                    dp_table_transpose[i][j] = 0
                else:
                    dp_table_transpose[i][j] = dp_table_transpose[i + 1][j + 1] + 1
                i -= 1
                j -= 1
            i, j = st_i, st_j
            while i >= 0:
                if matrix[i][j] == 0:
                    dp_table_move_upon[i][j] = 0
                else:
                    dp_table_move_upon[i][j] = dp_table_move_upon[i + 1][j] + 1
                i -= 1
            st_j -= 1
        depbug = [[0 for _ in range(len(matrix[0]) + 1) ]for _ in range(len(matrix) + 1)]

        cnt = 0
        i, j = len(matrix) - 1, len(matrix[0]) - 1
        # while i >= 0:
        #     while j >= 0:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cnt += min(dp_table_transpose[i][j],
                           dp_table_move_right[i][j],
                           dp_table_move_upon[i][j])
                depbug[i][j] = min(dp_table_transpose[i][j],
                           dp_table_move_right[i][j],
                           dp_table_move_upon[i][j])
                j -= 1
            i -= 1
        for i in depbug:
            print(i)

        return cnt




    def countSquares_recur(self, matrix):
        def move_upon(i, j):
            if i >= len(matrix):
                return 0
            if matrix[i][j] == 0:
                return 0
            return move_upon(i + 1, j) + 1

        def move_right(i, j):
            if j >= len(matrix[0]):
                return 0
            if matrix[i][j] == 0:
                return 0
            return move_right(i, j + 1) + 1

        def batckward(i, j):
            if i >= len(matrix) or j >= len(matrix[0]):
                return 0
            if matrix[i][j] == 0:
                return 0
            return batckward(i + 1, j + 1) + 1

        cnt = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    cnt += min(move_right(i, j), move_upon(i, j), batckward(i, j))
        return cnt


s = Solution()
a = [[1,1,0,0,1],
     [1,0,1,1,1],
     [1,1,1,1,1],
     [1,0,1,0,1],
     [0,0,1,0,1]]
print(s.countSquares(a))

