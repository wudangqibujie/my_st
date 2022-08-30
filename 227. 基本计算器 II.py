class Solution:
    def calculate(self, s):
        ix = 1
        stack = [s[0]]
        while ix < len(s):
            if s[ix] in ["/", "*"]:
                cal = s[ix]
                lst = ""
                while stack[-1] not in ["+", "-", "*", "/"]:
                    lst = stack.pop() + lst
                nxt = ""
                ix += 1
                while s[ix] not in ["+", "-", "*", "/"]:
                    nxt += s[ix]
                    ix += 1
                print(lst, cal, nxt)
                new_ = int(lst) // int(nxt) if cal == "/" else int(lst) * int(nxt)
                stack.append(str(new_))
                ix -= 1
            else:
                stack.append(s[ix])
            ix += 1
        print(stack)




s = Solution()
desc = "3+2*2/2+5/2+3-4/2"
desc = "3+2*2"
desc = " 3/2 "
desc = " 3+5 / 2 "
desc = "12+20/10*10"
print(s.calculate(desc))