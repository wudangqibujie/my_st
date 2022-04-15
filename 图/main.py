# 图真的没啥高深的，就是高级点的多叉树而已。

# // 邻接矩阵
# // graph[x] 存储 x 的所有邻居节点
# List<Integer>[] graph;

# // 邻接矩阵
# // matrix[x][y] 记录 x 是否有一条指向 y 的边
# boolean[][] matrix;

# 对于邻接表，好处是占用的空间少。
#
# 你看邻接矩阵里面空着那么多位置，肯定需要更多的存储空间。
#
# 但是，邻接表无法快速判断两个节点是否相邻。
#
# 比如说我想判断节点1是否和节点3相邻，我要去邻接表里1对应的邻居列表里查找3是否存在。但对于邻接矩阵就简单了，只要看看matrix[1][3]就知道了，效率高。

# 不过以我的经验呢，像网络流这种问题，你又不是打竞赛的，没时间的话就没必要学了；像 最小生成树 和 最短路径问题，虽然从刷题的角度用到的不多，
# 但它们属于经典算法，学有余力可以掌握一下；像 二分图判定、拓扑排序这一类，属于比较基本且有用的算法，应该比较熟练地掌握。

import copy
# 遍历图
graphs = {
    0: [3],
    1: [3],
    2: [],
    3: [6, 7],
    4: [5],
    5: [9],
    6: [],
    7: [9],
    8: [],
    9: []
}


def read_graph(graph):
    visted = set()

    def read(node):
        if node in visted:
            return
        print(node)
        visted.add(node)
        for nx in graph[node]:
            read(nx)

    for k in graph.keys():
        read(k)


# 判断图是否又换
def is_cycled(graph):
    is_cycle = False
    visted = set()

    def search(node, route):
        nonlocal is_cycle
        if node in route:
            is_cycle = True
            return
        route.append(node)
        for k in graph[node]:
            # new_route = copy.deepcopy(route)
            search(k, route)
        route.pop() # Attention!!!!

    for k in graph.keys():
        if k in visted:
            continue
        search(k, [])
        visted.add(k)
    return is_cycle


print(is_cycled(graphs))


# 拓扑排序
# 直观地说就是，让你把一幅图「拉平」，而且这个「拉平」的图里面，所有箭头方向都是一致的
# 很显然，如果一幅有向图中存在环，是无法进行拓扑排序的，因为肯定做不到所有箭头方向一致；反过来，如果一幅图是「有向无环图」，那么一定可以进行拓扑排序。
# 将后序遍历的结果进行反转，就是拓扑排序的结果。

