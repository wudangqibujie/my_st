class Solution:
    def topKFrequent(self, nums, k):
        log = dict()
        for i in nums:
            if i not in log:
                log[i] = 1
            else:

                log[i] += 1
        l = list(log.items())
        l.sort(key=lambda x: x[1], reverse=True)
        rs = []
        print(l)
        for i in range(k):
            rs.append(l[i][0])
        return rs


s = Solution()
nums = [1,1,1,2,2,3]
k = 2
s.topKFrequent(nums, k)