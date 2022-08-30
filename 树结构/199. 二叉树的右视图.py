# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from queue import Queue

class Solution:
    def rightSideView(self, root):
        que = Queue()
        que.put(root)
        rs = []
        while que.qsize():
            buff_que = Queue()
            flg = True
            while que.qsize():
                nxt = que.get()
                if nxt:
                    buff_que.put(nxt.right)
                    buff_que.put(nxt.left)
                    if flg:
                        rs.append(nxt.val)
                        flg = False
            que = buff_que
        return rs

s = Solution()
tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.left.left = TreeNode(4)
# tree.left.right = TreeNode(5)
# tree.left.right.left = TreeNode(6)
# tree.right = TreeNode(3)
print(s.rightSideView(tree))




