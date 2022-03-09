# 快速排序就是个二叉树的前序遍历，归并排序就是个二叉树的后续遍历，那么我就知道你是个算法高手了。
# 一旦你发现题目和子树有关，那大概率要给函数设置合理的定义和返回值，在后序位置写代码了。
# 只有后序位置才能通过返回值获取子树的信息。


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)


node3.right = node6
node1.right = node3
node2.left = node4
node2.right = node5
node1.left = node2


def mid_recur(node):
    if node is None:
        return
    print(node.val)
    mid_recur(node.left)
    mid_recur(node.right)


def pre_recur(node):
    if node is None:
        return
    pre_recur(node.left)
    print(node.val)
    pre_recur(node.right)


def post_recur(node):
    if node is None:
        return
    post_recur(node.left)
    post_recur(node.right)
    print(node.val)







