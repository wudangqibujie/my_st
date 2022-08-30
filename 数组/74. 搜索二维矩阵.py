class Solution:
    def searchMatrix(self, matrix, target):
        l_ix = len(matrix) - 1
        while l_ix >= 0 and matrix[l_ix][0] > target:
            l_ix -= 1
        if target == matrix[l_ix][0]:
            return True
        lst = matrix[l_ix]
        l, r = 0, len(lst)
        while l < r:
            # print(l, r)
            mid = (r + l) // 2
            if target == lst[mid]:
                return True
            elif target > lst[mid]:
                l = mid + 1
            else:
                r = mid
        return False





matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
matrix = [[1, 2], [3, 5]]
target = 4
so = Solution()
print(so.searchMatrix(matrix, target))