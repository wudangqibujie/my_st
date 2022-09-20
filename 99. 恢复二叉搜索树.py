# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        rslt = []
        rslt_node = []
        rslt_parent_node = []
        def read(node, parent_node, direction=None):
            if node is None:
                return
            read(node.left, node, "left")
            rslt.append(node.val)
            rslt_parent_node.append([parent_node, direction])
            rslt_node.append(node)
            read(node.right, node, "right")

        read(root, None, None)
        for ix in range(len(rslt_node)):
            p = rslt_parent_node[ix][0].val if rslt_parent_node[ix][0] else "None"
            # print(rslt_node[ix].val, p)
        rslt_sort = sorted(rslt)
        need = []
        for ix in range(len(rslt)):
            if rslt_sort[ix] != rslt[ix]:
                need.append(ix)
        if not need:
            return
        ix1, ix2 = need
        print(rslt)
        print(rslt_sort)
        print(need)

        node1, node2 = rslt_node[ix1], rslt_node[ix2]
        node1.val, node2.val = node2.val, node1.val
        print(root.val, root.left.val, root.right)

# root = TreeNode(1)
# root.left = TreeNode(3)
# root.left.right = TreeNode(2)


root = TreeNode(1)
# root.left = TreeNode(3)
# root.right = TreeNode(4)
# root.right.left = TreeNode(2)

# root = TreeNode(7)
# root.left = TreeNode(2)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right = TreeNode(6)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(4)

s = Solution()
rs = s.recoverTree(root)