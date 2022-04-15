class Solution:
    def findErrorNums(self, nums):
        ans1 = 0
        # for i in range(1, len(nums)+1):
        #     nums.append(i)
        # print(nums)
        for i in nums:
            ans1 = ans1 ^ i
        print(ans1)


s = Solution()
nums = [1,2,2,4]
print(s.findErrorNums(nums))

