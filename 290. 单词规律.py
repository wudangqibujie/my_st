class Solution:
    def wordPattern(self, pattern, s):
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        log = dict()
        rv_log = dict()
        for ix in range(len(pattern)):
            if pattern[ix] in log:
                if log[pattern[ix]] != words[ix]:
                    return False
            else:
                log[pattern[ix]] = words[ix]

            if words[ix] in rv_log:
                if rv_log[words[ix]] != pattern[ix]:
                    return False
            else:
                rv_log[words[ix]] = pattern[ix]
        # print(log)
        return True


s = Solution()
pattern = "abba"
ss = "dog dog dog dog"
print(s.wordPattern(pattern, ss))