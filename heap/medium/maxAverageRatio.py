from heapq import *

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        def profit(a, b):
            return (a + 1) / (b + 1) - a / b

        heap = [[-profit(a, b), a, b] for a, b in classes]
        heapify(heap)

        for _ in range(extraStudents):
            _, a, b = heappop(heap)
            heappush(heap, [-profit(a + 1, b + 1), a + 1, b + 1])

        return sum(a / b for _, a, b in heap) / len(classes)

    
print(Solution().maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2)) # 0.78333