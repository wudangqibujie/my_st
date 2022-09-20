# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from queue import Queue
class Solution:
    def addOneRow(self, root, val, depth):
        if root is None:
            return
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        que = Queue()
        que.put(root)
        ix = 1
        while que.qsize():
            que_buff = Queue()
            debug = []
            m = []
            while que.qsize():
                pop_node = que.get()
                if pop_node is None:
                    continue
                debug.append(pop_node)
                m.append(pop_node.val)
                que_buff.put(pop_node.left)
                que_buff.put(pop_node.right)
            que = que_buff
            if ix == depth - 1:
                for nd in debug:
                    # if nd.left:
                    l = nd.left
                    nd.left = TreeNode(val)
                    nd.left.left = l
                    # if nd.right:
                    r = nd.right
                    nd.right = TreeNode(val)
                    nd.right.right = r
                break
            ix += 1
        return root


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)


s = Solution()
val = 5
depth = 4
n = s.addOneRow(tree, val, depth)
def read(node):
    if node is None:
        return
    print(node.val)
    read(node.left)
    read(node.right)

read(n)
# print(n.val)
# print(n.left.val)
# print(n.left.left.val)
# print(n.left.left.left.val)
