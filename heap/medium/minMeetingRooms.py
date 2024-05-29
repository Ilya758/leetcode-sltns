from heapq import *


class Solution:
    def minMeetingRooms(self, A: list[list[int]]) -> int:
        A.sort()
        heap = [A[0][1]]

        for i in range(1, len(A)):
            start, end = A[i]

            if heap[0] <= start:
                heappop(heap)
            
            heappush(heap, end)

        return len(heap)

print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]])) # 2