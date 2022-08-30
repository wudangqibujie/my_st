class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find(i, j):
            # print(i, j)
            if i > j:
                return
            mid = (i + j) // 2
            # print(mid)
            mid_val = nums[mid]
            left_val = nums[mid - 1] if mid - 1 >= 0 else float("-inf")
            right_val = nums[mid + 1] if mid + 1 < len(nums) else float("-inf")
            # print(left_val, mid_val, right_val)
            if mid_val > left_val and mid_val > right_val:
                return mid
            if mid_val < right_val and mid_val >= left_val:
                return find(mid, j)
            if mid_val < left_val and mid_val >= right_val:
                return find(i, mid)
            if mid_val <= left_val and mid_val <= right_val:
                rs1 = find(mid, j)
                rs2 = find(i, mid)
                if rs1: return rs1
                if rs2: return rs2
        rs = find(0, len(nums))
        return rs


nums = [1, 3 ,2]
import random
random.shuffle(nums)
print(nums)
s = Solution()
print(s.findPeakElement(nums))