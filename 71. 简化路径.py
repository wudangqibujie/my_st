class Solution:
    def simplifyPath(self, path):
        paths = []
        ix = 0
        while ix < len(path):
            jx = 1
            while jx < len(path):
                if path[jx] == '/' and (jx - ix) > 1:
                    break
                jx += 1
            val = path[ix: jx]
            if val.startswith('//'):
                val = val[1: ]
            paths.append(val)
            ix = jx
        print(paths)
        stack = ['root']
        for p in paths:
            print("as", stack)
            if p == '/..':
                if stack[-1] == 'root':
                    continue
                stack.pop()
            elif p == '/.' or p == '/':
                continue
            else :
                stack.append(p)
        print(stack)
        if not stack:
            return '/'
        if stack[0] == 'root' and len(stack) == 1:
            return '/'
        if stack[0] == 'root' and len(stack) != 1:
            stack = stack[1: ]

        print(stack)
        if stack[-1] == '/' and len(stack) > 1:
            stack.pop()
        return ''.join(stack)



path = "/a/./b/../..//c/..."
# path = "/home//foo/"
path = "/../"
path = "/home/"
# path = "/a/./b/../../c/"
# path = '//./a/../a'
# path = "/a//b////c/d//././/.."
# path = "/home/../../.."
# path = "/.././em/jl///../.././../E/"
s = Solution()
print("rs", s.simplifyPath(path))