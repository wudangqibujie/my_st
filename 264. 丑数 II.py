import heapq
class Solution:
    def nthUglyNumber(self, n):
        rs = [1]
        # heapq.heappush(rs, 1)
        # print(heapq.heappop(rs))
        s = set()
        i = 1
        while i < n + 1:

            top = heapq.heappop(rs)
            # print(i, top)
            if top in s:
                continue
            if i == n:
                return top
            heapq.heappush(rs, top * 2)
            heapq.heappush(rs, top * 3)
            heapq.heappush(rs, top * 5)
            s.add(top)
            i += 1





s = Solution()
print(s.nthUglyNumber(10))