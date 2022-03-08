class Solution:
    def convertToTitle(self, columnNumber):
        letter_list = ["a", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        letter_list = [i.upper() for i in letter_list]
        rs = ""

        while columnNumber != 0:
            rs += letter_list[columnNumber // 26]
            columnNumber = (columnNumber % 26)
            print(columnNumber, rs)
        return rs



s = Solution()
s.convertToTitle(28)