class Solution:
    def merge(self, intervals):
        rs = sorted(intervals, key=lambda key: key[0])
        print(rs)
        stack = [rs[0]]
        for i in rs[1: ]:
            if stack[-1][-1] < i[0]:
                stack.append(i)
                continue
            new_i = stack[-1][0]
            new_j = max(stack[-1][1], i[1])
            stack.pop()
            stack.append([new_i, new_j])
        return stack


s = Solution()
intervals = [[1,4],[2,3], [4, 9], [5, 6]]
print(s.merge(intervals))