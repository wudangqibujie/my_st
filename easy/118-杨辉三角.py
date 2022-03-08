class Solution:
    def generate(self, numRows):
        numRows += 1
        if not numRows:
            return []
        rs = [[1]]

        for _ in range(1, numRows):
            buff_rs = []
            lst_rs = rs[-1]
            for i in range(len(lst_rs)+1):
                if i == 0 or i == len(lst_rs):
                    buff_rs.append(1)
                    continue
                val = lst_rs[i] + lst_rs[i-1]
                buff_rs.append(val)
            rs.append(buff_rs)
            rs = [buff_rs]
        return rs[0]

s = Solution()
print(s.generate(1))
