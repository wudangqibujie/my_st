import copy
class Solution:
    def combinationSum2(self, candidates, target):
        rs = []
        def backward(route, reeded, val):
            if val > target:
                return
            if val == target:
                rs.append(route)
            for i in range(len(candidates)):
                print(reeded)
                if i not in reeded:
                    new_route = copy.deepcopy(route)
                    new_route.append(candidates[i])
                    new_reed = copy.deepcopy(reeded)
                    new_reed.append(i)
                    backward(new_route, reeded, val + candidates[i])
        backward([], [], 0)
        return rs






s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(s.combinationSum2(candidates, target))