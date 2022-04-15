# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k):
        if not root:
            return
        rs = ["A"]
        def helper(node):
            if node is None:
                return 0
            helper(node.left)
            rs.append(node.val)
            helper(node.right)
        helper(root)
        return rs[k]





