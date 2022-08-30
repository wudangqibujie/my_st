# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        def search(node):
            if node is None:
                return []
            # print(node.val)
            rs_left = search(node.left)
            rs_right = search(node.right)
            rs = []
            for i in rs_left:
                rs.append(f"->{node.val}" + i)
            for i in rs_right:
                rs.append(f"->{node.val}" + i)
            if not rs:
                rs.append(f"->{node.val}")
            return list(set(rs))

        rs_l = search(root.left)
        rs_r = search(root.right)
        rs = list(set(rs_l + rs_r))
        # print(rs)
        if not rs:
            return [str(root.val)]
        for i in range(len(rs)):
            rs[i] = f"{root.val}" + rs[i]
        return rs

tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.left.right = TreeNode(5)
#
# tree.right = TreeNode(3)
s = Solution()
print(s.binaryTreePaths(tree))
