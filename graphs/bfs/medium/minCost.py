from collections import defaultdict
from heapq import *


class Solution:
    def minCost(self, n: int, roads: list[list[int]], appleCost: list[int], k: int) -> list[int]:
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u - 1].append((v - 1, w))
            graph[v - 1].append((u - 1, w))
        
        def find(i):
            weights = [float('inf')] * n
            heap = [(0, i)]
            weights[i] = appleCost[i]

            while heap:
                cost, node = heappop(heap)

                for nei, w in graph[node]:
                    nextCost = cost + w + w * k + appleCost[nei]

                    if nextCost < weights[nei]:
                        weights[nei] = nextCost
                        heappush(heap, (nextCost - appleCost[nei], nei))

            return min(weights)

        return [find(i) for i in range(n)]
    
print(Solution().minCost(n = 4, roads = [[1,2,4],[2,3,2],[2,4,5],[3,4,1],[1,3,4]], appleCost = [56,42,102,301], k = 2)) # [54,42,48,51]