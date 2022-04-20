class Solution:
    def subSort(self, array):
        if len(array) < 2:
            return [-1, -1]
        stack = [(0, array[0])]
        ix = 1
        font = [None for _ in range(len(array))]
        while stack and ix < len(array):
            while stack and stack[-1][-1] > array[ix]:
                pop_idx, pop_val = stack.pop()
                font[pop_idx] = ix
            stack.append((ix, array[ix]))
            ix += 1
        while stack:
            pop_idx, pop_val = stack.pop()
            font[pop_idx] = -1

        stack = [(len(array) - 1, array[-1])]
        ix = len(array) - 2
        rear = [None for _ in range(len(array))]
        while stack and ix >= 0:
            while stack and stack[-1][-1] < array[ix]:
                pop_idx, pop_val = stack.pop()
                rear[pop_idx] = ix
            stack.append((ix, array[ix]))
            ix -= 1
        while stack:
            pop_idx, pop_val = stack.pop()
            rear[pop_idx] = -1
        rs = []
        i = 0
        while i < len(array):
            if font[i] != -1:
                break
            i += 1
        rs1 = -1 if i == len(array) else i
        i = len(array) - 1
        while i >= 0:
            if rear[i] != -1:
                break
            i -= 1
        rs2 = -1 if i == -1 else i
        print(rs1, rs2)
        return [rs1, rs2]

s = Solution()
a =  [1, 2, 3, 9, 4, 5, 6, 7]
print(s.subSort(a))