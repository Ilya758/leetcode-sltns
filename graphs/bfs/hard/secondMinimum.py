from collections import defaultdict
from heapq import *


class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        heap = [(0, 1)]
        seen = [0] * (n + 1)
        dist = [float('inf')] * (n + 1)
        
        while heap:
            cost, node = heappop(heap)
            
            if dist[node] == cost or seen[node] > 1:
                continue
            
            seen[node] += 1
            dist[node] = cost
            
            if node == n and seen[node] > 1:
                return dist[node]
            
            if (cost // change) % 2 != 0:
                cost = (cost // change + 1) * change
            
            for nei in graph[node]:
                heappush(heap, (cost + time, nei))
        
        return -1
    
print(Solution().secondMinimum(5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5))