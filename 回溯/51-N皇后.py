import copy

class Solution:
    def solveNQueens(self, n):
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
                    backward(new_route, lvl_idx+1)
        backward([], 0)
        str_rs = []
        for can_blk in rs:
            buff_rs = []
            for ix in can_blk:
                a = ["." for _ in range(n)]
                a[ix] = "Q"
                buff_rs.append("".join(a))
            str_rs.append(buff_rs)
        return str_rs

s = Solution()
print(s.solveNQueens(4))