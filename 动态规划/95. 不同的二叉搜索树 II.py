# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n):
        nums = [i for i in range(1, n + 1)]
        # print(nums)

        def helper(l, r):
            if l == r:
                return [None]
            if (r - l) == 1:
                return [TreeNode(nums[l])]
            rs = []
            for ix in range(l, r):

                left = helper(l, ix)
                right = helper(ix + 1, r)
                # print(ix, l, r, left, right)
                for ll in left:
                    for rr in right:
                        node = TreeNode(nums[ix])
                        node.left = ll
                        node.right = rr
                        rs.append(node)
            return rs
        rs = helper(0, n)
        # print(len(rs))
        # for n in rs:
        #     print(n.val)
        return rs

s = Solution()
print(s.generateTrees(2))