# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root):
        if not root:
            return
        val_lst = []
        node_lst = []

        def read(node):
            if node is None:
                return
            read(node.left)
            val_lst.append(node.val)
            node_lst.append(node)
            read(node.right)
        read(root)
        lst = 0
        i = len(val_lst)-1
        while i >= 0:
            val_lst[i] = lst + val_lst[i]
            lst = val_lst[i]
            i -= 1
        for i in range(len(val_lst)):
            node_lst[i].val = val_lst[i]
        return tree





tree = TreeNode(4)
tree.left = TreeNode(1)
tree.right = TreeNode(6)

tree.left.left = TreeNode(0)
tree.left.right = TreeNode(2)
tree.left.right.right = TreeNode(3)

tree.right.left = TreeNode(5)
tree.right.right = TreeNode(7)
tree.right.right.right = TreeNode(8)

s = Solution()
rs = s.convertBST(tree)


def read(node):
    if node is None:
        return
    read(node.left)
    print(node.val)
    read(node.right)

read(rs)