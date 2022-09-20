# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0., next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        pre = ListNode(float("-inf"))
        tmp_pre = None
        tmp_now = pre

        point_node = head
        while point_node:
            # print(point_node.val, "PPPP")
            next_point_node = point_node.next
            while tmp_now is not None and point_node.val > tmp_now.val:
                tmp_pre = tmp_now
                tmp_now = tmp_now.next
            if tmp_now is None:
                # print("NONE")
                point_node.next = None
                tmp_pre.next = point_node
            else:
                # print("TMP", tmp_now.val)
                tmp_pre.next = point_node
                point_node.next = tmp_now
            point_node = next_point_node
            tmp_pre = None
            tmp_now = pre
        return pre.next


s = Solution()
head = ListNode(-1)
# head.next = ListNode(5)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(0)


node = s.insertionSortList(head)
print("********************")
while node:
    print(node.val)
    node = node.next