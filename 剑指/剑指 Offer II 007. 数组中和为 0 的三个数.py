class Solution:
    def threeSum(self, nums):
        nums.sort()
        print(nums)
        if len(nums) < 3:
            return []
        rs = []
        readed = set()
        for ix in range(1, len(nums) - 1):
            if nums[ix] in readed:
                continue
            mid_val = nums[ix]
            i, j = 0, len(nums) - 1
            print(ix, i, j)
            while ix > i and j > ix:
                print(i, j, ix)
                if ix == i or ix == j:
                    break
                if mid_val + nums[i] + nums[j] > 0:
                    j -= 1
                elif mid_val + nums[i] + nums[j] < 0:
                    i += 1
                else:
                    rs.append([nums[i], nums[j], nums[ix]])
                    break
            readed.add(nums[ix])
        return rs




# [-4, -1, -1, 0, 1, 2]

s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))
# [[-1,-1,2],[-1,0,1]]