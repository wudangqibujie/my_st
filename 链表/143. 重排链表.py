# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        node = head
        stack = []
        while node:
            stack.append(node)
            node = node.next
        i, j = 0, len(stack) - 1
        l = None
        while i <= j:
            stack[i].next = stack[j]
            # print(stack[i].val, stack[j].val)
            if l is not None:
                l.next = stack[i]
            l = stack[j]
            i += 1
            j -= 1
        l.next = None


head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

s = Solution()
s.reorderList(head)
node = head
while node:
    print(node.val)
    node = node.next