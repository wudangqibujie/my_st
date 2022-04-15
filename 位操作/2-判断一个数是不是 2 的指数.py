def solution(a):
    # 要判断是否2的指数，根据二进制计算公式，那么其二进制是只有1 个 1的，那么就可以用n & n - 1的法则判断有几个1
    rs = a & (a - 1)
    return rs == 0

print(solution(32))