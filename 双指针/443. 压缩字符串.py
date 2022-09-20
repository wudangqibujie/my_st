class Solution:
    def compress(self, chars):
        i, j = 0, 0
        wr_ix = 0
        while j < len(chars):
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            add = "" if (j - i) == 1 else str(j - i)
            # print(i, j, add)
            if (j - i) == 1:
                chars[wr_ix] = chars[i]
                i = j
                wr_ix += 1
                continue
            s = f"{chars[i]}{add}"
            # print(s)
            for ix in range(len(s)):
                chars[wr_ix + ix] = s[ix]
            # print(chars)
            wr_ix += len(s)
            # print(wr_ix, "WW")
            i = j
        print(chars)
        return wr_ix


s = Solution()
chars = ["a","a","b","b","c","c","c"]
# chars = ["a"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# chars = ["1", "b", "v"]
chars = ["a","a","a","a","a","b"]
print(s.compress(chars))