class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def find(i, j, k, h):
            # print(i, j, k, h)
            l = i
            while l <= j and matrix[l][k] <= target:
                if matrix[l][k] == target:
                    return True
                l += 1
            # [i: l - 1]
            r = j
            while r >= i and matrix[r][h] >= target:
                if matrix[r][h] == target:
                    return True
                r -= 1
            # [r + 1: j]
            if r + 1 > l - 1:
                return False
            a = k
            while a <= h and matrix[i][a] <= target:
                if matrix[i][a] == target:
                    return True
                a += 1
            # [k: a - 1]
            b = h
            while b >= k and matrix[j][b] >= target:
                if matrix[j][b] == target:
                    return True
                b -= 1
            # [b + 1: h]
            if b + 1 > a - 1:
                return False
            return find(r + 1, l - 1, b + 1, a - 1)
        return find(0, len(matrix) - 1, 0, len(matrix[0]) - 1)


s = Solution()
matrix = [[1]]
target = 1
print(s.searchMatrix(matrix, target))