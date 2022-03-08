class Solution:
    def titleToNumber(self, columnTitle):
        letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        letter_list = [i.upper() for i in letter_list]
        num_map = {letter_list[i]: i+1 for i in range(len(letter_list))}
        rs = 0
        columnTitle = columnTitle[::-1]

        for ix in range(len(columnTitle)):
            rs += (num_map[columnTitle[ix]] * (26 ** ix))
        return rs



s = Solution()
print(s.titleToNumber("BA"))
