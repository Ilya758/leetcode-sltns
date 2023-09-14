from collections import defaultdict
from heapq import *


class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        graph = defaultdict(int)

        for u, v in roads:
            graph[u] += 1
            graph[v] += 1
        
        edges = [-x for x in graph.values()]
        heapify(edges)
        ans = 0

        while edges:
            x = heappop(edges)
            ans += -x * n 
            n -= 1

        return ans
    
print(Solution().maximumImportance(n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])) # 43