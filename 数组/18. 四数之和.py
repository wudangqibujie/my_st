from copy import deepcopy
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        sum_log = dict()
        # print(nums)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum_val = nums[i] + nums[j]
                if sum_val in sum_log:
                    sum_log[sum_val].append([i, j])
                else:
                    sum_log[sum_val] = [[i, j]]
        rslt = []

        def find_target(fake_target, idxes):
            i, j = 0, len(nums) - 1
            rslt = []
            while i < j:
                if nums[i] + nums[j] == fake_target:
                    if i in idxes or j in idxes:
                        i += 1
                        j -= 1
                        continue
                    rslt.append(idxes + [i, j])
                    i += 1
                    j -= 1
                    continue
                elif nums[i] + nums[j] > fake_target:
                    j -= 1
                else:
                    i += 1
            return rslt

        signaure = set()
        for k, v in sum_log.items():
            fake_target = target - k
            # print(k, v, fake_target)
            # print(v)
            for x in v:
                candi_idxes = find_target(fake_target, x)
                if candi_idxes:
                    for candi_idx in candi_idxes:
                        candi_idx_ = [str(nums[i]) for i in sorted(candi_idx)]
                        sig = ",".join(candi_idx_)
                        if sig in signaure:
                            continue
                        # print("RS", candi_idx)
                        signaure.add(sig)
                        rslt.append([nums[i] for i in candi_idx])
        return rslt


nums = [1,0,-1,0,-2,2]
target = 0
nums = [0,-2,2,2,2]
target = 6
s = Solution()
print(s.fourSum(nums, target))