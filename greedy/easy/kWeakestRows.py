#  https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
from heapq import *


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        heap = []
        heapify(heap)

        for i, row in enumerate(mat):
            heappush(heap, (row.count(1), i))

        return [heappop(heap)[1] for _ in range(k)]


print(Solution().kWeakestRows(mat=[[1, 1, 0, 0, 0],
                                   [1, 1, 1, 1, 0],
                                   [1, 0, 0, 0, 0],
                                   [1, 1, 0, 0, 0],
                                   [1, 1, 1, 1, 1]],
                              k=3))  # [2, 0, 3]
