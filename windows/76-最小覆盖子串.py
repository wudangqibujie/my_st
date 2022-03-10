class Solution:
    def minWindow(self, s, t):
        st_idx = 0
        char_log = dict()

        def check(status):
            pass


        for i in t:
            if i not in char_log:
                char_log[i] = 1
                continue
            char_log[i] += 1

        while st_idx < len(s):
            if s[st_idx] in t:
                break
            st_idx += 1
        i, j = st_idx, st_idx + 1
        log_dict = dict()
        log_dict[s[i]] = 1
        while 1:
            # 右指针向右扩张情况

            if s[j] not in t:
                j += 1
            else:
                # 更新状态
                # 判断状态
                if check(log_dict):# 符合要求，则收缩左指针
                    i += 1
                else: # 不符合要求，继续扩大右指针
                    j += 1




# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
