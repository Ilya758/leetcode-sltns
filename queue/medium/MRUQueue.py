from collections import deque
from math import *


class MRUQueue:

    def __init__(self, n: int):
        self.sqrt = ceil(sqrt(n))
        nums = list(range(1, n + 1))
        chunks = [nums[i:i+self.sqrt] for i in range(0, n, self.sqrt)]
        self.buckets = [deque(chunk) for chunk in chunks]

    def fetch(self, k: int) -> int:
        k -= 1
        bucketIdx = k // self.sqrt
        itemIdx = k % self.sqrt
        bucket = self.buckets[bucketIdx]
        item = bucket[itemIdx]
        newChunk = deque([bucket[i] for i in range(len(bucket)) if i != itemIdx])
        self.buckets[bucketIdx] = newChunk
        self.buckets[-1].append(item)

        for i in range(bucketIdx, len(self.buckets) - 1):
            left, right = self.buckets[i], self.buckets[i + 1]
            left.append(right.popleft())

        return item


obj = MRUQueue(10)
print(obj.buckets)
obj.fetch(5)