from copy import deepcopy
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        stop = 10 ** n
        l = [str(i) for i in range(1, 10)]
        l_lst = deepcopy(l)
        cnt = 0
        for k in range(4):
            buff = []
            for ix in range(len(l)):
                val = f"{l_lst[ix]}{l[ix]}"
                buff.append(val)
                if int(val) <= stop:
                    cnt += 1
            # print(buff)
            l_lst = deepcopy(buff)
        return stop - cnt


s = Solution()
m = 2
print(s.countNumbersWithUniqueDigits(m))