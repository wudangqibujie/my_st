class Solution:
    def findRedundantConnection(self, edges):

        lao = [1 for _ in range(len(edges))]
        map_ = dict()
        for i in edges:
            map_[i[0]] = i[1]
        # def read(node, ix):




