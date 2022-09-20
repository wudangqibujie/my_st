# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head:
            return
        def merge(n1, n2):
            new = ListNode(1)
            head = new
            while n1 or n2:
                if n1 is None:
                    head.next = n2
                    n2 = n2.next
                    head = head.next
                    continue
                if n2 is None:
                    head.next = n1
                    n1 = n1.next
                    head = head.next
                    continue
                if n1.val < n2.val:
                    head.next = n1
                    n1 = n1.next
                else:
                    head.next = n2
                    n2 = n2.next
                head = head.next
            return new.next
        def cut(node):
            slow, fast = node, node
            l = None
            flg = 1
            while fast:
                if flg % 2 == 0:
                    l = slow
                    slow = slow.next
                flg += 1
                fast = fast.next
            l.next = None
            return node, slow

        def func(node):
            if node.next is None:
                return node
            s, f = cut(node)
            # print(node.val, ">>>>>>>>>>>>", s.val, f.val)
            if s.next is None and f.next is None:
                if s.val > f.val:
                    new = f
                    f.next = s
                    s.next = None
                else:
                    new = s
                    s.next = f
                    f.next = None
                return new
            else:
                rs_s = func(s)
                rs_f = func(f)
                new = merge(rs_s, rs_f)
                return new

        return func(head)





head = ListNode(11)
# head.next = ListNode(5)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(0)
# head.next.next.next.next.next = ListNode(7)

s = Solution()
rs = s.sortList(head)
while rs:
    print(rs.val)
    rs = rs.next