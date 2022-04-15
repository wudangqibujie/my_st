class Solution:
    def hammingWeight(self, n):
        cnt = 0
        while n != 0:
            cnt += 1
            n = n & (n - 1)
        return cnt


s = Solution()
print(s.hammingWeight(11))


# a = 9
# b = a - 1
# print(bin(a))
# print(bin(b))
# print(bin(a & b), a & b)
# print(a & b & (b - 1))
# print(int("00000000000000000000000000001011", 2))
