# 给你一幅「图」，请你用两种颜色将图中的所有顶点着色，且使得任意一条边的两个端点的颜色都不相同，你能做到吗？
#
# 这就是图的「双色问题」，其实这个问题就等同于二分图的判定问题，如果你能够成功地将图染色，那么这幅图就是一幅二分图，反之则不是：

# 二分图结构在某些场景可以更高效地存储数据

# 比如，如何存储电影演员和电影之间的关系？ 如果用哈希表存储，需要两个哈希表分别存储「每个演员到电影列表」的映射和「每部电影到演员列表」的映射。
# 但如果用「图」结构存储，将电影和参演的演员连接，很自然地就成为了一幅二分图

# 判定二分图的算法很简单，就是用代码解决「双色问题」。
# 说白了就是遍历一遍图，一边遍历一遍染色，看看能不能用两种颜色给所有节点染色，且相邻节点的颜色都不相同。




















