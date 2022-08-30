# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root):

        def helper(node):
            if node.left is None and node.right is None:
                return str(node.val)
            left = helper(node.left) if node.left else []
            right = helper(node.right) if node.right else []
            rs = str(node.val)
            lst = []
            for l in left:
                lst.append(rs + l)
            for r in right:
                lst.append(rs + r)
            return lst

        rs = helper(root)

        rs = [int(i.lstrip("0")) for i in rs if i.lstrip("0")]

        return sum(rs)


# tree = TreeNode(4)
# tree.left = TreeNode(9)
# tree.left.left = TreeNode(5)
# tree.left.right = TreeNode(1)
# tree.right = TreeNode(0)
# tree.right.right = TreeNode(1)
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

s = Solution()
print(s.sumNumbers(tree))
# print(495+491+401)

