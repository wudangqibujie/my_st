# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        i_flg = 1
        flg = True
        pre_i = None
        pre_j = None
        node_i = head
        fast_node = head
        node_j = head
        stp = 1
        while fast_node:
            if i_flg < k:
                pre_i = node_i
                node_i = node_i.next
                i_flg += 1
            if stp > k:
                pre_j = node_j
                node_j = node_j.next
            stp += 1
            fast_node = fast_node.next
        # print(pre_i, pre_j)
        if pre_i:
            pre_i.next = node_j
        if pre_j:
            pre_j.next = node_i
        tmp = node_i.next
        node_i.next = node_j.next
        node_j.next = tmp
        if pre_i is None:
            return node_j
        if pre_j is None:
            return node_i
        return head


head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
s = Solution()
n = s.swapNodes(head, 1)
while n:
    print(n.val)
    n = n.next