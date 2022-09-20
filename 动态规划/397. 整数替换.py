class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        map_ = dict()
        def find(val):
            if val == 1:
                return 0
            if val % 2 == 0:
                if val // 2 in map_:
                    rslt = map_[val // 2]
                else:
                    rslt = find(val // 2)
            else:
                if val - 1 in map_:
                    rslt1 = map_[val - 1]
                else:
                    rslt1 = find(val - 1)
                if val + 1 in map_:
                    rslt2 = map_[val + 1]
                else:
                    rslt2 = find(val + 1)
                rslt = min(rslt1, rslt2)
            return rslt + 1

        return find(n)


s = Solution()
n = 1
print(s.integerReplacement(n))