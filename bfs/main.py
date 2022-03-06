# BFS 的核心思想应该不难理解的，就是把一些问题抽象成图，从一个点开始，向四周开始扩散。一般来说，我们写 BFS 算法都是用「队列」这种数据结构，每次将一个节点周围的所有节点加入队列。

# BFS 相对 DFS 的最主要的区别是：BFS 找到的路径一定是最短的，但代价就是空间复杂度比 DFS 大很多

# 要说框架的话，我们先举例一下 BFS 出现的常见场景好吧，问题的本质就是让你在一幅「图」中找到从起点start到终点target的最近距离，这个例子听起来很枯燥，但是 BFS 算法问题其实都是在干这个事儿。

# 净整些花里胡哨的，这些问题都没啥奇技淫巧，本质上就是一幅「图」，让你从一个起点，走到终点，问最短路径。这就是 BFS 的本质，框架搞清楚了直接默写就好。


# DFS 不能找最短路径吗？其实也是可以的，但是时间复杂度相对高很多。

# 你想啊，DFS 实际上是靠递归的堆栈记录走过的路径，你要找到最短路径，肯定得把二叉树中所有树杈都探索完才能对比出最短的路径有多长对不对？

# 而 BFS 借助队列做到一次一步「齐头并进」，是可以在不遍历完整棵树的条件下找到最短距离的。

# 形象点说，DFS 是线，BFS 是面；DFS 是单打独斗，BFS 是集体行动。这个应该比较容易理解吧。

# BFS 可以找到最短距离，但是空间复杂度高，而 DFS 的空间复杂度较低。
from queue import Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.link_nodes = []


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
# node1.link_nodes = [node2, node4]
node1.link_nodes = [node2, node4, node3]
node2.link_nodes = [node3]
node4.link_nodes = [node2, node5]
node5.link_nodes = [node3, node2]


def fin_min_dis(st_node, target):
    rs = 0
    que = Queue()
    que.put(st_node)
    readed = []
    while que.qsize():
        buff_queue = Queue()
        for _ in range(que.qsize()):
            pop_node = que.get()
            if pop_node.val == target:
                return rs
            for link_node in pop_node.link_nodes:
                if link_node in readed:
                    continue
                buff_queue.put(link_node)
        rs += 1
        que = buff_queue


print(fin_min_dis(node1, 3))

