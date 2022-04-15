# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


tree = TreeNode(3)
tree.left = TreeNode(5)
tree.right = TreeNode(1)
tree.left.left = TreeNode(6)
tree.left.right = TreeNode(2)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(4)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(8)


def read(node):
    if node is None:
        return
    # print(node.val)
    read(node.left)
    read(node.right)


read(tree)


class Solution:
    def lowestCommonAncestor(self, root, p, q):

        def search(node):
            if node is None:
                return None
            if node.val == p:
                return node
            if node.val == q:
                return node
            left_s = search(node.left)
            right_s = search(node.right)
            if left_s and right_s:
                return node
            if left_s is None and right_s is None:
                return None
            rs = left_s if left_s else right_s
            return rs
        return search(root)

s = Solution()
rs = s.lowestCommonAncestor(tree, 5, 1)
print(rs.val)

