from heapq import *
from math import floor


def minStoneSum(piles: list[int], k: int) -> int:
    piles = [-pile for pile in piles]
    heapify(piles)

    while k:
        k -= 1
        pile = -(floor(heappop(piles) / 2))
        heappush(piles, -pile)

    return -sum(piles)


print(minStoneSum(piles=[5, 4, 9], k=2))  # 12
print(minStoneSum(piles=[4, 3, 6, 7], k=3))  # 12
