from typing import List
from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = defaultdict(list)

        for u, v, w in highways:
            graph[u].append((w, v))
            graph[v].append((w, u))

        dist = [[float('inf') for _ in range(discounts + 1)] for _ in range(n)]
        heap = [(0, 0, discounts)]
        seen = set()

        while heap:
            cost, node, d = heappop(heap)

            if (node, d) in seen:
                continue

            seen.add((node, d))

            for nxtCost, nxtNode in graph[node]:
                if d:
                    aCost = cost + nxtCost // 2

                    if aCost < dist[nxtNode][d - 1]:
                        dist[nxtNode][d - 1] = aCost
                        heappush(heap, (dist[nxtNode][d - 1], nxtNode, d - 1))
                
                if cost + nxtCost < dist[nxtNode][d]:
                    dist[nxtNode][d] = cost + nxtCost
                    heappush(heap, (dist[nxtNode][d], nxtNode, d))
        
        res = min(dist[n - 1])

        return res if res != float('inf') else -1 

print(Solution().minimumCost(n =
6,
highways =
[[0,1,2],[1,3,4],[0,2,6],[2,3,8],[3,4,100],[4,5,200]],
discounts =
2)) # 156