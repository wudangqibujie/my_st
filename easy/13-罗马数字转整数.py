class Solution:
    def romanToInt(self, s):
        num_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        rs = 0
        for ix in range(len(s)):
            front_char = s[ix]
            if ix == len(s)-1:
                rs += num_map[front_char]
                return rs
            reer_char = s[ix+1]
            if num_map[front_char] < num_map[reer_char]:
                rs -= num_map[front_char]
            else:
                rs += num_map[front_char]

s = Solution()
a = "MCMXCIV"
print(s.romanToInt(a))



