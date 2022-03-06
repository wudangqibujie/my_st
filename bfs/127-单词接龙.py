from queue import Queue
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        visted_set = set()
        rs = 1
        que = Queue()
        que.put(beginWord)
        while que.qsize():
            buff_que = Queue()
            for _ in range(que.qsize()):
                pop_node = que.get()
                if pop_node == endWord:
                    return rs
                visted_set.add(pop_node)
                for word in wordList:
                    if abs(len(set(word) - set(pop_node))) == 1 and word not in visted_set:
                        buff_que.put(word)
            que = buff_que
            rs += 1
        return 0




s = Solution()
beginWord = "lost"
endWord = "miss"
wordList = ["most","mist","miss","lost","fist","fish"]
print(s.ladderLength(beginWord, endWord, wordList))

