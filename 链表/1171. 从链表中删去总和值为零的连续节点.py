# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst = []
        tmp = head
        while tmp:
            lst.append(tmp.val)
            tmp = tmp.next
        # print(lst)
        cum_sum_lst = [0]
        pre = 0
        for i in lst:
            cum_sum_lst.append(i + pre)
            pre = cum_sum_lst[-1]
        map_ = dict()
        for ix, i in enumerate(cum_sum_lst):
            if i not in map_:
                map_[i] = [ix]
            else:
                map_[i].append(ix)
        gap = 0
        # print(cum_sum_lst)
        gap_info = (0, 0)
        print(map_)
        for k, v in map_.items():
            if len(v) < 2:
                continue
            if v[-1] - v[0] > gap:
                gap_info = (v[0], v[-1])
                gap = v[-1] - v[0]
        if gap == 0:
            return head

        for k, v in map_.items():
            if len(v) < 2:
                continue
            # if v[-1] - v[0] > gap:
            gap_info = (v[0], v[-1])
            gap = v[-1] - v[0]

            i, j = gap_info
            j -= 1
            # print(i, j)
            # print(head)
            node_i = head
            pre = None
            ix = 0
            while ix < i:
                pre = node_i
                node_i = node_i.next
                ix += 1

            node_j = node_i
            while ix < j:
                node_j = node_j.next
                ix += 1
            if pre:
                pre.next = node_j.next
            else:
                head = node_j.next
            # break
        return head



head = ListNode(-1)
head.next = ListNode(-2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(-1)
head.next.next.next.next = ListNode(0)
# [-1,-2,2,-1,0]
s = Solution()
n = s.removeZeroSumSublists(head)
print(n)
print("****************")
while n:
    print(n.val)
    n = n.next