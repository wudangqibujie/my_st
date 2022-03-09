import copy
class Solution:
    def allPathsSourceTarget(self, graph):
        routes = []

        def read(idx, route):
            # print(route)
            if route[-1] == len(graph) - 1:
                routes.append(route)
                return
            if len(graph[idx]) == 0:
                if route[-1] != len(graph) - 1:
                    return
                routes.append(route)
                return
            for nei in graph[idx]:
                new_route = copy.deepcopy(route)
                new_route.append(nei)
                read(nei, new_route)
        read(0, [0])
        return routes


graph = [[4,3,1],[3,2,4],[],[4],[]]
# graph = [[2],[],[1]]
s = Solution()
print(s.allPathsSourceTarget(graph))
