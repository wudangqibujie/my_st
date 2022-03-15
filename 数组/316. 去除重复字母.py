class Solution:
    def removeDuplicateLetters(self, s):
        count = dict()
        for s_ in s:
            if s_ not in count:
                count[s_] = 1
                continue
            count[s_] += 1
        print(count)

        readed = set()
        stack = []
        for ix in range(len(s)):
            if s[ix] in readed:
                continue
            while stack and ord(s[ix]) < ord(stack[-1]):
                if count[stack[-1]] > 1:
                    count[stack[-1]] -= 1
                    stack.pop()
                else:
                    break
            stack.append(s[ix])
            readed.add(s[ix])
        return stack


s = "cbacdcbc"
so = Solution()
print(so.removeDuplicateLetters(s))
