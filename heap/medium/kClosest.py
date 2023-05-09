from heapq import *
import math


def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    def calcDist(x: int, y: int) -> float:
        return math.sqrt(x * x + y * y)

    ans = []
    heap = []

    for i, (x, y) in enumerate(points):
        heappush(heap, (calcDist(x, y), i, (x, y)))

    while k:
        _, (x, y) = heappop(heap)
        k -= 1
        ans.append([x, y])

    return ans


print(kClosest(points=[[1, 3], [-2, 2]], k=1))  # [[-2,2]]
print(kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))  # [[3,3],[-2,4]]
