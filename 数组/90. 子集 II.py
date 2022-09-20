from copy import deepcopy


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rslt = [[] for _ in range(len(nums))]
        nums.sort()
        rslt[0] = [[nums[0]]]

        rs = [[nums[0]]]
        # print(nums)
        for ix in range(1, len(nums)):
            buff_rslt = []
            if nums[ix] in nums[: ix]:
                # print("BIN", rslt[ix - 1])
                for k in rslt[ix - 1]:
                    buff_rslt.append(k + [nums[ix]])
            else:
                buff_rslt.append([nums[ix]])
                # print(rslt[: ix])
                for j in rslt[: ix]:
                    for o in j:
                        buff_rslt.append(o + [nums[ix]])
            #     print(buff_rslt)
            # print(buff_rslt)
            rslt[ix] = buff_rslt
            rs.extend(buff_rslt)
        # print(rslt)
        rs.append([])
        return rs


s = Solution()
nums = [1, 2, 3, 3]
# nums = [0]
nums = [4,1,0]
print(s.subsetsWithDup(nums))


# [[],[0],[0,1],[0,1,4],[0,4],[1],[1,4],[4]]
# [[0], [1], [0, 1], [4], [0, 4], [1, 4], [0, 1, 4], []]