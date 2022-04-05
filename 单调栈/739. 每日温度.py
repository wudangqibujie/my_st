class Solution:
    def dailyTemperatures(self, temperatures):
        rs = [0 for _ in range(len(temperatures))]
        stack = [(temperatures[0], 0)]
        ix = 1
        while ix <= len(temperatures):
            if ix == len(temperatures):
                break
            while stack and temperatures[ix] > stack[-1][0]:
                pop_val, pop_idx = stack.pop()
                rs[pop_idx] = ix - pop_idx
            stack.append((temperatures[ix], ix))
            ix += 1
        return rs


s = Solution()
temperatures = [2, 1]
print(s.dailyTemperatures(temperatures))