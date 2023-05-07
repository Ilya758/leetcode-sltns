from heapq import *


class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -heappop(self.maxHeap))

        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (self.minHeap[0] - self.maxHeap[0]) / 2


medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())  # 1.5
medianFinder.addNum(3)
print(medianFinder.findMedian())  # return 2.0
