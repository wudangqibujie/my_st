# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        rs = None
        def search(node):
            if node is None:
                return
            print(node.val)
            if node.val == p.val or node.val == q.val:
                print("BIN")
                return True
            l = search(node.left)
            r = search(node.right)
            nonlocal rs
            if l and r:
                print("catch")
                if not rs:
                    rs = node
            if l or r:
                return True
            return
        search(root)
        return rs

tree = TreeNode(6)
tree.left = TreeNode(2)
tree.right = TreeNode(8)
tree.left.left = TreeNode(0)
tree.left.right = TreeNode(4)
tree.left.right.left = TreeNode(3)
tree.left.right.right = TreeNode(5)
tree.right.left = TreeNode(7)
tree.right.right = TreeNode(9)
p = TreeNode(6)
q = TreeNode(5)
s = Solution()
rs = s.lowestCommonAncestor(tree, p, q)
print(rs.val)
