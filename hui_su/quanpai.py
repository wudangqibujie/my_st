from copy import deepcopy
class Solution:
    def permute(self, nums):
        if not nums:
            return []
        rs = []
        def backwards(candis, route):
            if len(candis) == 0:
                rs.append(route)
                return
            for c in candis:
                new_candis = deepcopy(candis)
                new_ruotes = deepcopy(route)
                new_ruotes.append(c)
                new_candis.remove(c)
                backwards(new_candis, new_ruotes)

        backwards(nums, [])
        return rs
s = Solution()
print(s.permute([1, 2, 3]))