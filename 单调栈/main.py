

nums = [2,1,2,4,3]

def solution(nums):
    stack = []
    rs = [0 for _ in range(len(nums))]
    ix = 0
    while ix < len(nums):
        val = nums[ix]
        while stack and val > stack[-1][0]:
            pop_val, pop_idx = stack.pop()
            rs[pop_idx] = val
        stack.append([val, ix])
        ix += 1
    while stack:
        pop_val, pop_idx = stack.pop()
        rs[pop_idx] = -1
    print(rs)

solution(nums)
