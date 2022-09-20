# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        MAP = dict()
        def read(node):
            if node.val in MAP:
                # print(f"{node.val} readed!!")
                return MAP[node.val]
            new_node = Node(node.val)
            MAP[new_node.val] = new_node
            new_neight = []
            for ne_d in node.neighbors:
                # print(f"VAL: {node.val}, neight: {ne_d.val}")
                rs = read(ne_d)
                new_neight.append(rs)
            new_node.neighbors = new_neight
            return new_node
        return read(node)


node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)


# node1.neighbors = [node2, node4]
# node2.neighbors = [node1, node3]
# node3.neighbors = [node2, node4]
# node4.neighbors = [node1, node3]




s = Solution()
rs = s.cloneGraph(node1)


readed = set()
def read(node):
    if node.val in readed:
        return
    print(node.val)
    readed.add(node.val)
    for nd in node.neighbors:
        print(f"NODE :{node.val}, NE:{nd.val}")
        read(nd)

read(rs)