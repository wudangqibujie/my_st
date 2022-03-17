class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.now_capacity = 0
        self.map_ = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # 判断是否在列表
        #     不在，返回-1
        # 在
        #     取出值
        #     解除原有链表关系
        #     放到队列头部
        #     返回值
        print(key, self.map_)
        if not self.is_in_link(key):
            return -1
        else:
            rs_node = self.map_[key]  # 取出节点
            self.remove_from_link(key)  # 从双链表中去除该节点
            self.add_totail(key, rs_node.val)  # 把该节点重新添加回头部
            return rs_node.val

    def put(self, key, value):
        # 先判断是否在队列
        # 在队列
        #     解除原有关系，放到队列头部， 更新value值
        # 不在队列
        #     放到队列头部
        #     是否达到容量
        #         去除队尾的节点
        #     更新哈希表
        if self.is_in_link(key):
            self.remove_from_link(key)  # 解除链表中的关系
            self.add_totail(key, value)  # 重新加入队列头部
        else:
            self.add_totail(key, value)  # 加到队列头部
            print(self.now_capacity, "CAACA")
            if self.now_capacity > self.capacity:  # 如果超出容量，则解除队列尾部节点
                self.remove_from_head()

    def remove_from_head(self):
        # tmp = self.head.next
        if self.head.next == self.tail:
            return
        self.map_.pop(self.head.next.key)
        self.head.next.prev = self.head
        self.head.next = self.head.next.next
        self.now_capacity -= 1

    def add_totail(self, key, value):
        new_node = Node(key, value)
        tmp = self.tail.prev
        tmp.next = new_node
        new_node.prev = tmp
        new_node.next = self.tail
        self.tail.prev = new_node
        self.now_capacity += 1

    def is_in_link(self, key):
        return key in self.map_

    def remove_from_map(self, key):
        self.map_.pop(key)

    def remove_from_link(self, key):
        print("STEP", read_node(self.tail))
        node = self.map_[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        self.now_capacity -= 1
        self.map_.pop(key)


def read_node(tail):
    if tail is None:
        return
    print("读取   ", tail.key, tail.val)
    tail = tail.prev
    read_node(tail)


lru = LRUCache(2)
lru.put(1, 1)
read_node(lru.tail)
lru.put(2, 2)
print(lru.tail.prev.prev.key, lru.tail.prev.prev.prev.key, lru.tail.prev.prev.next.key)
print(lru.tail.prev.key, lru.tail.prev.next.key, lru.tail.prev.prev.key)
read_node(lru.tail)
print(lru.map_)
print("获取", lru.get(1))

read_node(lru.tail)
# print(lru.map_)
# print(lru.now_capacity)
