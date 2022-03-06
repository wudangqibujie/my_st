import copy

class Solution:
    def restoreIpAddresses(self, s):

        def isvald(s):
            if len(s) == 0:
                return False
            if len(s) != 1 and s.startswith("0"):
                return False
            if int(s) >= 0 and int(s) <= 255:
                return True
            return False

        rs = []
        def backward(route, left, lvl_idx):
            # print(route, left, lvl_idx)
            if lvl_idx == 4:
                if len(left) == 0:
                    ip_rs = ".".join(route)
                    if ip_rs not in rs:
                        rs.append(ip_rs)
                return

            for i in range(1, 4):
                # print(left, i)
                if isvald(left[: i]):
                    new_ip = left[: i]
                    new_route = copy.deepcopy(route)
                    new_route.append(new_ip)
                    backward(new_route, left[i: ], lvl_idx+1)
        backward([], s, 0)
        return rs

s = Solution()
ip = "1"
print(s.restoreIpAddresses(ip))







