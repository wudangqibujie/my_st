class Solution:
    def findComplement(self, num):
        stop_cnt = 0
        val = num
        while val != 0:
            stop_cnt += 1
            val = val >> 1
        # print(bin(num), stop_cnt)


        ans = 1
        for _ in range(stop_cnt-1):
            ans = (ans << 1) + 1
        # print(bin(ans))
        return (num ^ ans)

s = Solution()
print(s.findComplement(1))


