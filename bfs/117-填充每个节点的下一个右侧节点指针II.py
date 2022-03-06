
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return None
        tmp = root
        que = Queue()
        que.put(root)
        while que.qsize():
            buff_que = Queue()
            lst = None
            for _ in range(que.qsize()):
                pop_node = que.get()
                if pop_node is None:
                    continue
                pop_node.next = lst
                lst = pop_node
                buff_que.put(pop_node.right)
                buff_que.put(pop_node.left)
            que = buff_que
        return tmp