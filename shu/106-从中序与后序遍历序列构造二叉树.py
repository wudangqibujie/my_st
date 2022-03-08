# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        idx = len(inorder)
        if not inorder:
            return
        def helper(i, j):
            if i >= j:
                return
            nonlocal idx
            idx -= 1
            for k in range(i, j):
                if inorder[k] == postorder[idx]:
                    break
            # print(k, inorder[k], postorder[idx], idx)
            node = TreeNode(postorder[idx])
            right_node = helper(k + 1, j)
            left_node = helper(i, k)
            node.right = right_node
            node.left = left_node
            return node
        return helper(0, len(inorder))

s = Solution()
inorder = [3,2,4]
postorder = [3,4,2]
rs = s.buildTree(inorder, postorder)

def read(node):
    if node is None:
        return
    read(node.left)
    print(node.val)
    read(node.right)

read(rs)