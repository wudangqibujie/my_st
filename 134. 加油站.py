class Solution:
    def canCompleteCircuit(self, gas, cost):
        ind = [0]
        for ix in range(len(gas)):
            ind.append((gas[ix] - cost[ix]) + ind[ix])
        ind = ind[1: ]



s = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(s.canCompleteCircuit(gas, cost))