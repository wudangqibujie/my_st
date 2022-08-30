class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            print(i, j)
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                if nums[j] > target:
                    i = mid
                else:
                    j = mid
            else:
                if nums[i] < target:
                    j = mid
                else:
                    i = mid
        return False


s = Solution()
nums = [2,5,6,0,0,1,2]
target = 0
nums = [2,5,6,0,0,1,2]
target = 3
print(s.search(nums, target))
