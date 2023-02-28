class Solution:
    def trailingZeroes(self, n):
        if n == 0 or n == 1:
            return 0
        debug = [1]
        count = 0
        mark = [1]
        for i in range(2, n + 1):
            debug.append(debug[-1] * i)
            val = mark[-1] * i
            val_str = str(val)
            ix = len(val_str) - 1
            while ix >= 0 and val_str[ix] == '0':
                ix -= 1
                count += 1
            mark.append(int(val_str[ix]))
        print(debug)
        print(mark)
        print(len(debug), len(mark))
        for ix in range(len(debug)):
            print(debug[ix], mark[ix], ix+2)
        return count



nn = 2
while True:
    rslt = 1
    for i in range(1, nn + 1):
        rslt *= i
    rslt = str(rslt)
    # print(rslt)
    c = 0
    ix = len(rslt) - 1
    while ix >= 0 and rslt[ix] == '0':
        c += 1
        ix -= 1

    s = Solution()
    rslt1 = s.trailingZeroes(nn)
    if rslt1 != c:
        print(nn)
        print(rslt1, c)
        print(print(rslt))

        break

    nn += 1
