# 想在迭代代码中体现前中后序遍历，关键点在哪里？
#
# 当我从栈中拿出一个节点p，我应该想办法搞清楚这个节点p左右子树的遍历情况。
#
# 如果p的左右子树都没有被遍历，那么现在对p进行操作就属于前序遍历代码。
#
# 如果p的左子树被遍历过了，而右子树没有被遍历过，那么现在对p进行操作就属于中序遍历代码。
#
# 如果p的左右子树都被遍历过了，那么现在对p进行操作就属于后序遍历代码。

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


node1 = Node(1)
node1.left = Node(2)
node1.right = Node(3)
node1.left.right = Node(4)
"""
      1
     / \
    2   3
     \
      4
"""
def inter_post(tree):
    stack = []
    rs = []
    stack.append(tree)
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if hasattr(node, "visted"):
            rs.append(node.val)
        else:
            stack.append(node)
            stack.append(node.right)
            stack.append(node.left)
            node.visted = True
    print(rs)


def inter_pre(tree):
    stack = []
    rs = []
    stack.append(tree)
    while stack:
        node = stack.pop()
        if node is None:
            continue
        rs.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
    print(rs)


def inter_mid(tree):
    stack = []
    rs = []
    stack.append(tree)
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if hasattr(node, "visted"):
            rs.append(node.val)
        else:
            node.visted = True
            stack.append(node.right)
            stack.append(node)
            stack.append(node.left)
    print(rs)


inter_post(node1)
