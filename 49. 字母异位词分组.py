import random
class Solution:
    def groupAnagrams(self, strs):
        alpha = dict()
        for i in range(97, 123):
            alpha[chr(i)] = i

        cal_mp = dict()
        for ix in range(len(strs)):
            key_log = [0 for _ in range(26)]
            for ix_str in strs[ix]:
                key_log[alpha[ix_str] - 97] += 1
            print(strs[ix])
            print(key_log)
            key = ",".join([str(i) for i in key_log])
            if key in cal_mp:
                cal_mp[key].append(strs[ix])
            else:
                cal_mp[key] = [strs[ix]]
        print(cal_mp)
        return list(cal_mp.values())




s = Solution()
strs = ["bdddddddddd","bbbbbbbbbbc"]
print(s.groupAnagrams(strs))

