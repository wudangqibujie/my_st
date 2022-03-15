from queue import Queue
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


node1 = Node(1)
node1.left = Node(2)
node1.right = Node(3)
node1.left.right = Node(4)


def lvl_serialize(node):
    que = Queue()
    rs = ""
    que.put(node)
    while que.qsize():
        print(que.qsize())
        node = que.get()
        if node is None:
            rs += ",#"
            continue
        rs += f",{node.val}"
        que.put(node.left)
        que.put(node.right)
    return rs.lstrip(",")


se_rs = lvl_serialize(node1)

def unserilizer(rs):
    rs_lst = rs.split(",")
    que = Queue()
    que.put(0)
    # 左 2i + 1 右 2i + 2
    while que.qsize():
        pop_idx = que.get()
        que.put(2 * pop_idx + 1)
        que.put(2 * pop_idx + 2)
        node = Node(rs_lst[pop_idx])
