class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        cols = ((len(s) // (numRows + (numRows - 2))) + 1) * (numRows - 1)
        log = [["" for _ in range(cols)] for _ in range(numRows)]
        ix = 0
        st_x, st_y = 0, 0
        while ix < len(s):
            while ix < len(s) and st_x < numRows:
                log[st_x][st_y] = s[ix]
                ix += 1
                st_x += 1
            st_x = numRows - 2
            st_y += 1
            while ix < len(s) and st_x > 0:
                log[st_x][st_y] = s[ix]
                st_y += 1
                st_x -= 1
                ix += 1
        return "".join(["".join(i) for i in log])




so = Solution()
s = "PALL"
numRows = 3
print(so.convert(s, numRows))