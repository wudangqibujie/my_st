# Definition for a binary tree node.
from queue import Queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root):
        rslt = []
        if not root:
            return rslt
        que = Queue()
        que.put(root)

        while que.qsize():
            rs = None
            nxt_que = Queue()
            while que.qsize():
                pop_node = que.get()
                if rs is None:
                    rs = pop_node.val
                rs = max(rs, pop_node.val)
                if pop_node.left:
                    nxt_que.put(pop_node.left)
                if pop_node.right:
                    nxt_que.put(pop_node.right)
            rslt.append(rs)
            que = nxt_que
        return rslt



tree = TreeNode(1)
tree.left = TreeNode(3)
tree.right = TreeNode(2)
tree.right.right = TreeNode(9)
tree.left.left = TreeNode(50)
tree.left.right = TreeNode(3)
tree.left.right.right = TreeNode(3)

s = Solution()
print(s.largestValues(tree))
