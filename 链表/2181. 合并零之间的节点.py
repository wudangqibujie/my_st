# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = head
        while node:
            if node.val == 0:
                node = node.next
            else:
                dyn_node = node
                while dyn_node and dyn_node.val != 0:
                    node.val += dyn_node.val
                    dyn_node = dyn_node.next
                node.next = dyn_node
                node = dyn_node
        node = head.next
        # print(node.val)
        pre = head
        while node:
            if node.val == 0:
                pass
            else:
                pre.next = node
                pre = node
            node = node.next
        return head.next

head = ListNode(0)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(0)

s = Solution()
n = s.mergeNodes(head)
while n:
    print(n.val)
    n = n.next