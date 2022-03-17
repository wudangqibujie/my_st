import math
import heapq


class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        if len(self.large) <= len(self.small):
            heapq.heappush(self.small, -num)
            pop_val = 0 - heapq.heappop(self.small)
            heapq.heappush(self.large, pop_val)
        else:
            heapq.heappush(self.large, num)
            pop_val = heapq.heappop(self.large)
            heapq.heappush(self.small, -pop_val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2

medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
medianFinder.addNum(3)
medianFinder.addNum(4)
medianFinder.addNum(-1000)
print(medianFinder.findMedian())
# print(medianFinder.small, medianFinder.large)