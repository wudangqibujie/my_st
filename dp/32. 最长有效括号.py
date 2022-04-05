class Solution:
    def longestValidParentheses(self, s):
        mx = 0
        for i in range(len(s)):
            j = i
            banlance = 0
            while j < len(s):
                if s[j] == "(":
                    banlance += 1
                else:
                    banlance -= 1
                if banlance < 0:
                    break
                if banlance == 0:
                    # print(j, i)
                    mx = max(mx, j - i + 1)
                j += 1
        print(mx)
        return mx


s = Solution()
a = ""
print(s.longestValidParentheses(a))


