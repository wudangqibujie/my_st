class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


node1 = Node(1)
node1.left = Node(2)
node1.right = Node(3)
node1.left.right = Node(4)


def solution(tree):
    rs = ""
    def helper(node):
        nonlocal rs
        if node is None:
            rs += ",#"
            return

        rs += f",{node.val}"
        helper(node.left)
        helper(node.right)
    helper(tree)
    return rs.lstrip(",")


seri_rs = solution(node1)


def deserialize(s):
    se_lst = s.split(",")
    print(se_lst)
    idx = 0
    def helper():
        nonlocal idx
        if idx == len(s):
            return
        if se_lst[idx] == "#":
            idx += 1
            return None
        node = Node(se_lst[idx])
        # print(se_lst[idx])
        idx += 1
        left_node = helper()
        right_node = helper()
        node.left = left_node
        node.right = right_node
        return node

    node = helper()
    return node


tr = deserialize(seri_rs)


def read(node):
    if node is None:
        return
    print(node.val)
    read(node.left)
    read(node.right)


read(tr)
