class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


node1 = Node(1)
node1.left = Node(2)
node1.right = Node(3)
node1.left.right = Node(4)


def serialize(node):
    rs = ""

    def helper(node):
        nonlocal rs
        if node is None:
            rs += ",#"
            return
        helper(node.left)
        helper(node.right)
        rs += f",{node.val}"
        return rs
    return helper(node).lstrip(",")

se_rs = serialize(node1)
print(se_rs)

def un_serialize(rs):
    rs_lst = rs.split(",")
    print(rs_lst)
    idx = len(rs_lst) - 1

    def helper():
        nonlocal idx
        if idx < 0:
            return
        if rs_lst[idx] == "#":
            idx -= 1
            return
        node = Node(rs_lst[idx])
        idx -= 1
        # print(node.val)
        node.right = helper()
        node.left = helper()

        return node
    return helper()


tr = un_serialize(se_rs)
def read(node):
    if node is None:
        return
    print(node.val)
    read(node.left)
    read(node.right)


read(tr)
