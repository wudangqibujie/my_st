class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            if nums[0] == 0:
                return 0
        st = 0
        cnt = 1
        while True:
            print(st)
            print(st+1, st+1+nums[st])
            cand = nums[st + 1: st + 1 + nums[st]]
            if len(nums) - 1 in cand:
                return cnt
            nxt = max(nums[st + 1: st + 1 + nums[st]])
            st = nxt
            cnt += 1
        return cnt


s = Solution()
nums = [1, 2]
print(nums[1: 2])
print(s.jump(nums))
