import heapq

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        rs = [1]
        primes.sort()
        print(primes)
        # heapq.heappush(rs, 1)
        # print(heapq.heappop(rs))
        s = set()
        i = 1
        while i < n + 1:

            top = heapq.heappop(rs)
            if top in s:
                continue
            if i == n:
                return top
            # print(top)
            for j in primes:
                heapq.heappush(rs, top * j)
            # heapq.heappush(rs, top * 3)
            # heapq.heappush(rs, top * 5)
            s.add(top)
            i += 1

s = Solution()
n = 12
primes = [2,7,13,19]
print(s.nthSuperUglyNumber(n, primes))