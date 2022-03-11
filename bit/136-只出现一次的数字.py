class Solution:
    def singleNumber(self, nums):
        rs = 0
        for i in nums:
            rs ^= i
        return rs


s = Solution()
a = [4, 2, 2, 5, 5, 6 ,7 ,8, 8, 7 ,6]
# a = [1, 2, 2, 1, 4]
a = [1, 2, 3, 4, 5, 1, 2, 3, 4]
print(s.singleNumber(a))