
# Definition for a Node.
class Node:
    def __init__(self, x, next, random):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return
        tmp = head
        log = dict()
        log_ = dict()
        st = 0
        while tmp:
            log[st] = tmp
            log_[tmp] = st
            tmp = tmp.next
            st += 1

        new_head_pre = Node(-1, None, None)
        tmp = new_head_pre
        pre_tmp = head
        my_log = dict()
        flag = 0
        while pre_tmp:
            tmp.next = Node(pre_tmp.val, None, None)
            my_log[flag] = tmp.next
            pre_tmp = pre_tmp.next
            tmp = tmp.next
            flag += 1
        pre_tmp = head
        now_tmp = new_head_pre.next
        while pre_tmp:
            k = pre_tmp.random
            now_tmp.random = my_log[log_[k]] if k else None
            # print(now_tmp.val, pre_tmp.val)
            # print(log_)
            pre_tmp = pre_tmp.next
            now_tmp = now_tmp.next



        return new_head_pre.next





s = Solution()
node1 = Node(1, None, None)
node2 = Node(2, None, None)
node1.next = node2
node1.random = node2
node2.next = None
node2.random = node2

rs = s.copyRandomList(node1)
# rs = node7
while rs:
    print(rs.val)
    rn = rs.random
    if rn:
        print("RAM", rn.val)
    else:
        print("null")
    rs = rs.next
















