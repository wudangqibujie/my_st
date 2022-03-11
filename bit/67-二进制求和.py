class Solution:
    def addBinary(self, a, b):
        print(int(a, 2), int(b, 2))
        def add(x, y):
            if y == 0:
                return x
            pure_add = x ^ y
            additional = (x & y) << 1
            return add(pure_add, additional)

        return bin(add(int(a, 2), int(b, 2)))[2: ]

s = Solution()
a = "1010"
b = "1011"
print(s.addBinary(a, b))

# print(int("001101", 2))
#
# print(bin(4), 4)
# print(bin(5), 5)
# print(bin(4 & 5), "4 & 5")
# print(bin(4 | 5), "4 | 5")
