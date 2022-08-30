class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        tnt_idxes = []
        # print((len(mat) + len(mat[0]) - 2) + 1)
        for sum_ in range((len(mat) + len(mat[0]) - 2) + 1):
            st = 0
            idxes = []
            print(sum_)
            while st < len(mat):
                ed = sum_ - st
                if ed >= len(mat[0]) or ed < 0:
                    st += 1
                    continue
                idxes.append((st, ed))
                # print(st, ed)
                st += 1
            if sum_ % 2 == 0:
                idxes.reverse()
            tnt_idxes.extend(idxes)
        rslt = []
        for i, j in tnt_idxes:
            rslt.append(mat[i][j])
        return rslt
s = Solution()
mat = [[1,2,3],
       [4,5,6]]
print(s.findDiagonalOrder(mat))