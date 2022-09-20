# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from queue import Queue
class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        que = Queue()
        que.put(root)
        rs = 0
        while que.qsize():
            buff_que = Queue()
            lst = []
            while que.qsize():
                pop_node = que.get()
                lst.append(pop_node)
                if pop_node is None:
                    buff_que.put(None)
                    buff_que.put(None)
                    continue
                buff_que.put(pop_node.left)
                buff_que.put(pop_node.right)
            # print(lst)
            # print([i.val for i in lst if i])
            flg = True
            for i in lst:
                if i is not None:
                    flg = False
            if flg:
                break
            l, r = 0, len(lst) - 1
            while l < len(lst) and lst[l] is None:
                l += 1
            while r>= 0 and lst[r] is None:
                r -= 1
            que = buff_que
            if l <= r:
                rs = max(rs, r - l + 1)
        return rs


tree = TreeNode(1)
tree.left = TreeNode(3)
tree.left.left = TreeNode(5)
tree.left.left.left = TreeNode(5)

tree.left.right = TreeNode(3)
tree.right = TreeNode(2)
tree.right.right = TreeNode(9)
tree.right.right.right = TreeNode(9)

s = Solution()
print(s.widthOfBinaryTree(tree))