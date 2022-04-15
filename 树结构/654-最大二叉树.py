# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return
        def helper(i, j):
            # print(i, j)
            if i >= j:
                return
            if (j - i) == 1:
                return TreeNode(nums[i])
            mid_idx = None
            flag = float("-inf")
            for ix in range(i, j):
                val = nums[ix]
                if val > flag:
                    flag = val
                    mid_idx = ix
            # print(flag, "FLAG", mid_idx, i, j)
            node = TreeNode(flag)
            left_node = helper(i, mid_idx)
            right_node = helper(mid_idx + 1, j)
            node.left = left_node
            node.right = right_node
            return node
        return helper(0, len(nums))


s = Solution()
a = [3, 5]
rs = s.constructMaximumBinaryTree(a)
# print(rs.val)

def read(node):
    if node is None:
        return
    print(node.val)
    read(node.left)
    read(node.right)

read(rs)


