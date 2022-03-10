
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        rs = []
        if not root:
            return rs
        def search(node):
            if node is None:
                return
            rs.append(node.val)
            for n in node.children:
                search(n)
        search(root)
        return rs