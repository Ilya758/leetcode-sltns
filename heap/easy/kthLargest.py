
from heapq import *


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        heapify(nums)
        self.heap = nums
        self.k = k

        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)

        if len(self.heap) > self.k:
            heappop(self.heap)

        return self.heap[0]


kthLargest = KthLargest(3, [4, 5, 8, 2])
kthLargest.add(3)
kthLargest.add(5)
kthLargest.add(10)
kthLargest.add(9)
kthLargest.add(4)
