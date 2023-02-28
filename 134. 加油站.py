class Solution:
    def canCompleteCircuit(self, gas, cost):
        log = []
        for ix in range(len(gas)):
            log.append(gas[ix] - cost[ix])
        # print(log)
        mo = [0]
        for ix in range(len(log)-1):
            mo.append(mo[ix] + log[ix])
        flag = mo[-1] + log[-1]
        # print(mo)
        if flag < 0:
            return -1
        idx = mo.index(min(mo))
        return idx


s = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas = [2,3,4]
cost = [3,4,3]

gas = [4, 51,2,3]
cost = [1, 2, 3,4,5]

gas = [2, 1]
cost = [1, 1]
print(s.canCompleteCircuit(gas, cost))