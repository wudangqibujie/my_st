# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        node_num = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            node_num += 1
        slices = [node_num // k for _ in range(k)]
        ix = 0
        for _ in range(node_num - (node_num // k) * k):
            slices[ix % len(slices)] += 1
            ix += 1
        print(slices)
        st = head
        pre = None
        tmp = head
        rslt = []
        for sl in slices:
            for _ in range(sl):
                pre = tmp
                tmp = tmp.next
            if pre is None:
                rslt.append(None)
                continue
            pre.next = None
            rslt.append(st)
            st = tmp
            pre = None
        print(rslt)
        return rslt


node = ListNode(1)
head = node
# for i in range(2, 4):
#     new = ListNode(i)
#     head.next = new
#     head = new

s = Solution()
rs = s.splitListToParts(node, 1)

for ix, i in enumerate(rs):
    print("************", ix)
    n = i
    while n:
        print(n.val)
        n = n.next