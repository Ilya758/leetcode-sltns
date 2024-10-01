from heapq import *


class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort()
        ans = day = i = 0
        n = len(events)
        heap = []

        while i < n or heap:
            if not heap:
                day = events[i][0]

            while i < n and events[i][0] <= day:
                heappush(heap, events[i][1])
                i += 1

            heappop(heap)
            day += 1
            ans += 1

            while heap and heap[0] < day:
                heappop(heap)

        return ans
    
print(Solution().maxEvents([[3,4],[3,4],[3,4]])) # 2