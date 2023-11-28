from collections import Counter, deque
from heapq import *

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        q = deque()
        counter = Counter(tasks)
        ans = 0
        heap = [-v for v in counter.values()]
        heapify(heap)

        while heap or q:
            ans += 1

            if heap:
                v = heappop(heap) + 1

                if v < 0:
                    q.append([v, ans + n])

            if q and q[0][1] == ans:
                heappush(heap, q.popleft()[0])

        return ans
    

print(Solution().leastInterval(["A","A","A","B","B","B"], 50)) # 104