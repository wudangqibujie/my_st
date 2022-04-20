import heapq
class Solution:
    def nthUglyNumber(self, n, a, b, c):
        p = [a, b, c]
        p.sort()
        a, b, c = p
        rs = [1]
        # heapq.heappush(rs, 1)
        # print(heapq.heappop(rs))
        s = set()
        i = 1
        while i < n + 2:

            top = heapq.heappop(rs)
            print(i, top)
            if top in s:
                continue
            if i == n + 1:
                return top
            heapq.heappush(rs, top * a)
            heapq.heappush(rs, top * b)
            heapq.heappush(rs, top * c)
            s.add(top)
            i += 1

s = Solution()
n = 5
a = 2
b = 11
c = 13
print(s.nthUglyNumber(n, a, b, c))