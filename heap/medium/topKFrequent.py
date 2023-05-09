from collections import Counter
from heapq import *


def topKFrequent(words: list[str], k: int) -> list[str]:
    heap = [(-freq, word) for word, freq in Counter(words).items()]
    heapify(heap)

    return [heappop(heap)[1] for _ in range(k)]


print(topKFrequent(words=["the", "day", "is", "sunny", "the", "the",
      "the", "sunny", "is", "is"], k=4))  # ["the","is","sunny","day"]
