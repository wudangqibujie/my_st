import copy
class Solution:
    def totalNQueens(self, n):
        rs = []

        def is_valid(route_set, lvl_idx, candi):
            for ix, val in enumerate(route_set):
                if candi == val:
                    return False
                lft_val = val - (lvl_idx - ix)
                rht_val = val + (lvl_idx - ix)
                if lft_val == candi or rht_val == candi:
                    return False
            return True

        def backward(route, lvl_idx):

            if lvl_idx == n:
                rs.append(route)
                return
            for candi in range(n):
                if is_valid(route, lvl_idx, candi):
                    new_route = copy.deepcopy(route)
                    new_route.append(candi)
                    backward(new_route, lvl_idx + 1)

        backward([], 0)
        return len(rs)


s = Solution()
print(s.totalNQueens(1))