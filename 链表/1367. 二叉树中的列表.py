# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        if head is None or root is None:
            return
        def match(tree, link, is_matching):
            if link is None and is_matching:
                return True
            if tree is None:
                return False
            if tree.val == link.val:
                # print(tree.val, link.val)
                l = match(tree.left, link.next, True)
                r = match(tree.right, link.next, True)
                if any([l, r]):
                    return True
            else:
                return False
                # l = match(tree.left, link, False)
                # r = match(tree.right, link, False)
                # if any([l, r]):
                #     return True
                # else:
                #     return False
            return False

        flg = False
        candi = []
        def read(node):
            if node is None:
                return
            if node.val == head.val:
                candi.append(node)
            read(node.left)
            read(node.right)
        read(root)
        # print(candi)
        for tn in candi:
            # print(tn.val)
            rs = match(tn, head, True)
            # print(rs)
            if rs:
                return True
        return flg


tree = TreeNode(1)
tree.left = TreeNode(4)
tree.right = TreeNode(4)
tree.left.right = TreeNode(2)
tree.left.right.left = TreeNode(1)

tree.right.left = TreeNode(2)
tree.right.left.left = TreeNode(6)
tree.right.left.right = TreeNode(8)
tree.right.left.right.left = TreeNode(1)
tree.right.left.right.right = TreeNode(3)



node = ListNode(4)
node.next = ListNode(2)
node.next.next = ListNode(8)

s = Solution()
print(s.isSubPath(node, tree))