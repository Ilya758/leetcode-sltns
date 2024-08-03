from collections import defaultdict
from heapq import *


class StockPrice:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.latest = 0
        self.timestamps = defaultdict(int)
        self.prices = defaultdict(set)

    def update(self, t: int, p: int) -> None:
        if t in self.timestamps:
            oldPrice = self.timestamps[t]
            self.prices[oldPrice].remove(t)

            if not self.prices[oldPrice]:
                del self.prices[oldPrice]

        heappush(self.maxHeap, -p)
        heappush(self.minHeap, p)

        self.timestamps[t] = p
        self.prices[p].add(t)
        self.latest = max(self.latest, t)

    def current(self) -> int:
        return self.timestamps[self.latest]

    def maximum(self) -> int:
        while -self.maxHeap[0] not in self.prices:
            heappop(self.maxHeap)

        return -self.maxHeap[0]

    def minimum(self) -> int:
        while self.minHeap[0] not in self.prices:
            heappop(self.minHeap)

        return self.minHeap[0]