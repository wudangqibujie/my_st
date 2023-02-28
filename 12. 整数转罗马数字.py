class Solution:
    def intToRoman(self, num):
        num_lst = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        char_lst = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        num_lst.reverse()
        char_lst.reverse()
        res = ''
        while num:
            for i in range(len(num_lst)):
                if num_lst[i] <= num:
                    res += char_lst[i]
                    num -= num_lst[i]
                    break
        return res

s = Solution()
num = 3999
print(s.intToRoman(num))