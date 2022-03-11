a = 123
b = 321
c = a ^ b
d = a & b
e = a | b
f = a << 1
g = a >> 1
print(bin(a))
print(bin(b))
print(bin(c))
print(bin(d))
print(bin(e))
print(bin(f))
print(bin(g))
print(f, g)
# 0b 001111011
# 0b 101000001

# 0b 100111010 a ^ b
# 0b 001000001 a & b
# 0b 101111011 a | b

# >> 一次就是除以2一次，<< 就是乘以2一次
# 0b 001111011 a 123
# 0b 011110110 a << 1 246
# 0b 000111101 a >> 1 61

# 左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。
# 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数

# 二进制转十进制
print(int("110", 2))
print(a << 2)

# n & (n - 1)就是消去最后一位 1
for i in range(1000):
    # i += 0.123123
    print(bin(i - 1), i -1)
    print(bin(i), i)
    print(bin((i - 1) & i))
    print()

print(bin(-2), bin(2))