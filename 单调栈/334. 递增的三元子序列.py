class Solution:
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        stack = [(0, nums[0])]
        idx = 1
        log_fron = [-1 for _ in range(len(nums))]
        log_rear = [-1 for _ in range(len(nums))]
        while idx < len(nums):
            if nums[idx] < stack[-1][-1]:
                stack.append((idx, nums[idx]))
                idx += 1
                continue
            while stack and stack[-1][-1] < nums[idx]:
                pop_idx, pop_val = stack.pop()
                log_fron[pop_idx] = idx
            stack.append((idx, nums[idx]))
            idx += 1
        while stack:
            pop_idx, pop_val = stack.pop()
            log_fron[pop_idx] = -1

        idx = len(nums) - 2
        stack = [(len(nums) - 1, nums[-1])]
        while idx >= 0:
            if nums[idx] > stack[-1][-1]:
                stack.append((idx, nums[idx]))
                idx -= 1
                continue
            while stack and nums[idx] < stack[-1][-1]:
                pop_idx, pop_val = stack.pop()
                log_rear[pop_idx] = idx
            stack.append((idx, nums[idx]))
            idx -= 1
        while stack:
            pop_idx, pop_val = stack.pop()
            log_rear[pop_idx] = -1
        for i in range(1, len(nums) - 1):
            if log_rear[i] != -1 and log_fron[i] != -1:
                return True
        return False


s = Solution()
nums = [-1, 0, 1]
print(s.increasingTriplet(nums))
