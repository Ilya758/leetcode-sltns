from collections import defaultdict
from heapq import *


class Solution:
    def minimumDistance(self, n: int, edges: list[list[int]], s: int, marked: list[int]) -> int:
        graph = defaultdict(list)
        seen = set(marked)
        
        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [float('inf')] * n
        dist[s] = 0
        heap = [(0, s)]

        while heap:
            cost, u = heappop(heap)

            if u in seen:
                return cost
            if cost != dist[u]:
                continue

            for v, w in graph[u]:
                nxt = cost + w
                
                if nxt < dist[v]:
                    dist[v] = nxt
                    heappush(heap, (nxt, v))

        return -1

print(Solution().minimumDistance(n = 4, edges = [[0,1,1],[1,2,3],[2,3,2],[0,3,4]], s = 0, marked = [2,3])) # 4 