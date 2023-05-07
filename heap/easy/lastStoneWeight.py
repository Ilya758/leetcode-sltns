# https://leetcode.com/problems/last-stone-weight/description/

from heapq import *


def lastStoneWeight(stones: list[int]) -> int:
    stones = [-stone for stone in stones]
    heapify(stones)

    while len(stones) > 1:
        first = abs(heappop(stones))
        second = abs(heappop(stones))

        if second != first:
            heappush(stones, -abs(first - second))

    return -stones[0] if stones else 0


print(lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))  # 1
print(lastStoneWeight(stones=[1]))  # 1
