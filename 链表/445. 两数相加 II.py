# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next
        add_flg = 0
        lst_node = None
        while stack1 or stack2:
            pop_1 = stack1.pop().val if stack1 else 0
            pop_2 = stack2.pop().val if stack2 else 0
            val = pop_1 + pop_2 + add_flg
            sta_val = val % 10
            new_node = ListNode(sta_val)
            new_node.next = lst_node

            add_flg = int(val >= 10)
            lst_node = new_node
        if add_flg == 1:
            new_node = ListNode(1)
            new_node.next = lst_node
            lst_node = new_node
        return lst_node


n1 = ListNode(1)
# n1.next = ListNode(9)
# n1.next.next = ListNode(9)
# n1.next.next.next = ListNode(9)

n2 = ListNode(9)
# n2.next = ListNode(9)
# n2.next.next = ListNode(9)

s = Solution()
rs = s.addTwoNumbers(n1, n2)
while rs:
    print(rs.val)
    rs = rs.next