class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        i, j = 0, len(nums)
        # while i < j:
        #     mid = i + (j - i) // 2
        #     if nums[mid] > target:
        #         j = mid
        #     elif nums[mid] < target:
        #         i = mid + 1
        #     else:
        #         return True
        # return False
        while i < j:
            mid = i + (j - i) // 2
            print(i, mid, j, nums[i: j])
            if nums[i] >= nums[j - 1]:
                # print(i, mid, j)
                if nums[mid] == target:
                    return True
                else:
                    if target < nums[i]:
                        if nums[mid] > target:
                            j = mid
                        else:
                            i = mid + 1
                    elif target > nums[i]:
                        if nums[mid] > target:
                            i = mid + 1
                        else:
                            j = mid
                    else:
                        return True
            else:
                if nums[mid] > target:
                    j = mid
                elif nums[mid] < target:
                    i = mid + 1
                else:
                    return True
        return False




s = Solution()
nums = [2, 3, 0]
target = 0
nums = [2,5,6,0,0,1,2]
target = 0
nums = [2,5,6,0,0,1,2]
target = 3
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2
print(nums)
print(s.search(nums, target))
