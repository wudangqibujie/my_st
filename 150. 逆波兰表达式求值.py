from math import floor, ceil

class Solution:
    def evalRPN(self, tokens):
        stack = [tokens.pop()]
        # print(stack)
        # print(tokens)
        char_ = ["+", "-", "*", "/"]
        while stack:
            token = tokens.pop()
            if token in char_:
                stack.append(token)
                continue
            # print("stack: ", stack)
            if token not in char_ and stack[-1] not in char_:
                right_val = stack.pop()
                cal_char = stack.pop()
                if cal_char == '/':
                    new_rs = eval(f"int({token}{cal_char}{right_val})")
                else:
                    new_rs = eval(f"{token}{cal_char}{right_val}")
                # print(new_rs)
                tokens.append(str(new_rs))

            else:
                stack.append(token)
        # print(stack)
        return new_rs

s = Solution()
tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ['12', '0', '+']
print(s.evalRPN(tokens))
