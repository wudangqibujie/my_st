# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return
        idx = -1
        def helper(i, j):
            if i >= j:
                return None
            nonlocal idx
            idx += 1
            for k in range(i, j):
                if inorder[k] == preorder[idx]:
                    break
            node = TreeNode(preorder[idx])
            left_node = helper(i, k)
            right_node = helper(k+1, j)
            node.left = left_node
            node.right = right_node
            return node
        return helper(0, len(preorder))

s = Solution()
preorder = [1, 2, 3]
inorder = [3, 2, 1]
rs = s.buildTree(preorder,inorder)

def read(node):
    if node is None:
        return
    print(node.val)
    read(node.left)
    read(node.right)

read(rs)