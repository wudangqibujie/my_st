class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(n + 1)]
        # print(dp)
        for ix in range(2, len(dp)):
            if dp[ix] == 0:
                continue
            step = ix * ix
            
            while step * ix <= n:
                dp[step * ix] = 0
                step += 1
        #     print(dp)
        # print(dp[n])
        dp = dp[2: -1]
        print(dp)
        return sum(dp)




s = Solution()
print(s.countPrimes(10))


