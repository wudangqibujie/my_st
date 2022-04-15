# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root):
        rs = None
        def func(node):
            if node is None:
                return 0
            nonlocal rs
            left_val = func(node.left)
            right_val = func(node.right)
            left = left_val if left_val > 0 else 0
            right = right_val if right_val > 0 else 0
            new = node.val + left + right
            # print(new)
            if rs is None:
                rs = new
            else:
                rs = max(new, rs)
            return node.val + max(left, right)
        func(root)
        return rs

tree = TreeNode(-10)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

s = Solution()
print(s.maxPathSum(tree))