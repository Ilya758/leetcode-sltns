from collections import defaultdict
from heapq import *


class Solution:
    def minimumCost(self, n: int, A: list[list[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in A:
            graph[u].append((w, v))
            graph[v].append((w, u))

        heap = [(0, n)]
        seen = set()
        ans = 0

        while heap and len(seen) < n:
            w, v = heappop(heap)

            if v not in seen:
                seen.add(v)
                ans += w

                for c, nxt in graph[v]:
                    if nxt not in seen:
                        heappush(heap, (c, nxt))

        return ans if len(seen) == n else -1 
    
print(Solution().minimumCost(3, [[1,2,5],[1,3,6],[2,3,1]])) # 6