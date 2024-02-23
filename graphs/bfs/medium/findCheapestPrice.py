from collections import defaultdict
from heapq import *


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        if src not in graph:
            return -1

        q = [(0, src, k + 1)]
        dist = defaultdict(lambda: float('inf'))

        while q:
            cost, node, stops = heappop(q)

            if node == dst:
                return cost

            if stops > 0:
                for v, w in graph[node]:
                    temp = cost + w
                    
                    if temp < dist[(v, stops)]:
                        dist[(v, stops)] = temp
                        heappush(q, (temp, v, stops - 1))

        return -1

print(Solution().findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1)) # 700
