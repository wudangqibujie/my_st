# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if not head:
            return []
        t = head
        cnt = 0
        while t:
            t = t.next
            cnt += 1
        rslt = [0 for _ in range(cnt)]

        tmp = head
        stack = [(tmp, 0)]
        nxt = tmp.next
        ix = 1
        while nxt:
            while stack and stack[-1][0].val < nxt.val:
                pop, pop_ix = stack.pop()
                rslt[pop_ix] = nxt.val
            stack.append((nxt, ix))
            ix += 1
            nxt = nxt.next
        return rslt


head = ListNode(2)
# head.next = ListNode(7)
# head.next.next = ListNode(4)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(5)



s = Solution()
print(s.nextLargerNodes(head))