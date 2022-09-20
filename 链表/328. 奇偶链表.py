# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_node = head
        if not head:
            return
        even_node = head.next
        if even_node is None:
            return head

        pre = head
        mid = pre.next
        nxt = mid.next
        cnt = 0
        while nxt:
            cnt += 1
            pre.next = nxt
            pre = mid
            mid = nxt
            nxt = mid.next
        if cnt % 2 == 0:
            mid.next = None
            pre.next = even_node
        else:
            pre.next = None
            mid.next = even_node

        return odd_node


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)


s = Solution()
node = s.oddEvenList(head)
while node:
    print(node.val)
    node = node.next

