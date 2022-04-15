class Solution:
    def findCircleNum(self, isConnected):
        log = [None for _ in range(len(isConnected))]
        flg = 0
        def search(ix):
            if log[ix]:
                return
            log[ix] = str(flg)
            for i in range(len(isConnected[ix])):
                if isConnected[ix][i] != 0 and ix != i:
                    search(i)

        for ix in range(len(isConnected)):
            search(ix)
            # print(ix, log)
            flg += 1
        # print(log)
        return len(set(log))


s = Solution()
isConnected = [[1, 0], [0, 1]]
print(s.findCircleNum(isConnected))