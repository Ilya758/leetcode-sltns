from heapq import *


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        profits = sorted(zip(capital, profits))
        i = 0
        heap = []

        for _ in range(k):
            while i < len(profits) and profits[i][0] <= w:
                heappush(heap, -profits[i][1])
                i += 1

            if not heap:
                return w

            w -= heappop(heap)

        return w


print(Solution().findMaximizedCapital(
    k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))  # 4
print(Solution().findMaximizedCapital(
    k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]))  # 6
