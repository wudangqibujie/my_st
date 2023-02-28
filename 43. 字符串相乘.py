class Solution:
    def multiply(self, num1, num2):

        def multi_one(num):
            ix = len(num1) - 1
            scale = 1
            rslt = 0
            while ix >= 0:
                rslt += int(num1[ix]) * int(num) * scale
                ix -= 1
                scale *= 10
            return rslt

        scale = 1
        rslt = 0
        ix = len(num2) - 1
        while ix >= 0:
            rslt += multi_one(num2[ix]) * scale
            ix -= 1
            scale *= 10
        return str(rslt)


s = Solution()
num1 = "125"
num2 = "456"
num1 = "345534562"
num2 = "25345345"



print(s.multiply(num1, num2))
print(int(num1) * int(num2))