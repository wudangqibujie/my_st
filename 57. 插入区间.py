class Solution:
    def insert(self, intervals, newInterval):
        hold = []
        final_rs = []
        if intervals:
            end = max(intervals[-1][-1], newInterval[-1])
        else:
            end = max(0, newInterval[-1])
        bit1 = [0 for _ in range(end)]
        new1 = [0 for _ in range(end)]
        for inte in intervals:
            if inte[0] == inte[1]:
                hold.append(inte)
            for i in range(inte[0], inte[1]):
                bit1[i] = 1
        for i in range(newInterval[0], newInterval[1]):
            new1[i] = 1
        if newInterval[0] == newInterval[1]:
            hold.append(newInterval)
        rs = []
        for i in range(len(bit1)):
            rs.append(bit1[i] | new1[i])
        print(bit1)
        print(new1)
        print(rs)

        ix = 0
        while ix < len(bit1):
            if rs[ix] == 0:
                ix += 1
                continue
            tmp_ix = ix
            while ix < len(bit1) and rs[ix] == 1:
                ix += 1
            final_rs.append([tmp_ix, ix])
        r = []

        return r





s = Solution()
intervals = [[0,1],[5,5],[6,7],[9,11]]
newInterval = [12,21]
# [[0,1],[5,5],[6,7],[9,11]]
# [12,21]
print(s.insert(intervals, newInterval))
# [[0,1],[5,5],[6,7],[9,11],[12,21]]