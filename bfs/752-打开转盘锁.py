from queue import Queue
class Solution:
    def openLock(self, deadends, target):
        visted = set(deadends)
        visted.add("0000")
        rs = 0
        que = Queue()
        if "0000" in deadends:
            return -1
        que.put("0000")
        while que.qsize():
            buff_que = Queue()
            for _ in range(que.qsize()):
                pop_node = que.get()
                if pop_node == target:
                    return rs
                for i in range(4):
                    roll = int(pop_node[i])
                    up_roll = (roll+1) % 10
                    low_roll = roll - 1 if roll >= 1 else 9
                    char_lst = list(pop_node)

                    char_lst[i] = str(up_roll)
                    new_try1 = "".join(char_lst)

                    char_lst[i] = str(low_roll)
                    new_try2 = "".join(char_lst)
                    # print(new_try1, new_try2)
                    if new_try1 not in visted:
                        buff_que.put(new_try1)
                        visted.add(new_try1)

                    if new_try2 not in visted:
                        buff_que.put(new_try2)
                        visted.add(new_try2)

            rs += 1
            que = buff_que
        return -1



s = Solution()
deadends = ["0033","3201","0321","0122","3032","2120","1230","2303","2111","2030"]

target = "0123"

print(s.openLock(deadends, target))







