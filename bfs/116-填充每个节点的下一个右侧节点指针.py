
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

from queue import Queue
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

s = Solution()
new = s.connect(node1)
print(new.next)
print(new.left.next.val)
print(new.right.next)
print(new.left.left.next.val)
print(new.left.left.next.next.next.next)






