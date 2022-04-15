class Solution:
    def findOrder(self, numCourses, prerequisites):
        rs = []
        graph = dict()
        for p in prerequisites:
            if p[0] not in graph:
                graph[p[0]] = [p[1]]
            else:
                graph[p[0]].append(p[1])
        for ix in range(numCourses):
            if ix not in graph:
                graph[ix] = []
        # print(graph)
        visted = set()
        is_cycle = True

        def search(node, route):
            nonlocal is_cycle
            if node in route:
                is_cycle = False
                return
            if node in visted:
                return
            route.append(node)
            visted.add(node)
            for k in graph[node]:
                search(k, route)
            rs.append(node)
            route.pop()

        for k in graph.keys():
            if k in visted:
                continue
            search(k, [])
            visted.add(k)
        if is_cycle:
            return rs
        return []


s = Solution()
numCourses = 2
prerequisites = [[1,0]]
print(s.findOrder(numCourses, prerequisites))