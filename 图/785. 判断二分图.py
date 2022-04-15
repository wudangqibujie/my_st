class Solution:
    def isBipartite(self, graph):
        visted = set()
        is_bin_gph = True
        color = [None for _ in range(len(graph))]
        def search(node):
            nonlocal is_bin_gph
            if not is_bin_gph:
                return
            if node in visted:
                return
            if color[node] is None:
                color[node] = 1
            visted.add(node)
            for net in graph[node]:
                if color[net] is None:
                    color[net] = 0 if color[node] == 1 else 1
                    search(net)
                else:
                    if color[node] == color[net]:
                        is_bin_gph = False
        for ix in range(len(graph)):
            search(ix)
        return is_bin_gph

s = Solution()
graph = [[1,3],[0,2],[1,3],[0,2]]
print(s.isBipartite(graph))