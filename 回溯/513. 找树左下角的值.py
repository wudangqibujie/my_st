# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from queue import Queue
class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return
        que = Queue()
        que.put(root)
        rslt = []
        while que.qsize():
            nxt_que = Queue()
            while que.qsize():
                pop_node = que.get()
                if pop_node.right:
                    nxt_que.put(pop_node.right)
                if pop_node.left:
                    nxt_que.put(pop_node.left)
                rslt.append(pop_node.val)
            que = nxt_que
            if que.qsize() == 0:
                break
        return rslt[-1]



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.right.left = TreeNode(5)
tree.right.left.left = TreeNode(7)
tree.right.right = TreeNode(6)

s = Solution()
print(s.findBottomLeftValue(tree))