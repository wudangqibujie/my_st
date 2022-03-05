import copy
class Solution:
    def combinationSum(self, candidates, target):
        rs = []
        def backward(route, val):
            if val > target:
                return
            if val == target:
                bu = sorted(route)
                if bu not in rs:
                    rs.append(bu)
            for c in candidates:
                new_route = copy.deepcopy(route)
                new_route.append(c)
                backward(new_route, val + c)
        backward([], 0)
        return rs


s = Solution()
candidates = [2,3,6]
target = 20
print(s.combinationSum(candidates, target))
