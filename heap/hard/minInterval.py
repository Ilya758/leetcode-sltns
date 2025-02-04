from heapq import *


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        heap = []
        A = sorted(intervals)[::-1]
        cache = {}

        for q in sorted(queries):
            while A and A[-1][0] <= q:
                left, right = A.pop()

                if right >= q:
                    heappush(heap, (right - left + 1, right))

            while heap and heap[0][1] < q:
                heappop(heap)

            cache[q] = heap[0][0] if heap else -1

        return [cache[q] for q in queries]
    
print(Solution().minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5])) # [3,3,1,4]