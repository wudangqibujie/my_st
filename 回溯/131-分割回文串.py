import copy
class Solution:
    def partition(self, s):
        def is_reroll_str(s):
            # print(f"检测{s}")
            i, j = 0, len(s)-1
            while i <= j:
                if s[i] != s[j]:
                    return False
                j -= 1
                i += 1
            return True
        rs = []

        def backward(route, left):
            # print(route, f"* {left} *")
            if len(left) == 0:
                rs.append(route)
                return
            for i in range(1, len(left)+1):
                check_s = left[: i]
                # print(f"CHECK {check_s}")
                if is_reroll_str(check_s):
                    new_route = copy.deepcopy(route)
                    new_route.append(left[: i])
                    backward(new_route, left[i: ])

        backward([], s)
        return rs


s = Solution()
m = "bcaacb"
print(s.partition(m))