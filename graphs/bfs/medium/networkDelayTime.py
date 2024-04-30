from collections import defaultdict
from heapq import *


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u - 1].append((v - 1, w))

        def find():
            dist = [float('inf')] * n
            dist[k - 1] = 0
            heap = [(0, k - 1)]

            while heap:
                curDist, node = heappop(heap)
                
                if curDist != dist[node]:
                    continue
                
                for nei, w in graph[node]:
                    nextDist = curDist + w

                    if nextDist < dist[nei]:
                        dist[nei] = nextDist
                        heappush(heap, (nextDist, nei))

            return dist

        ans = max(find())

        return -1 if ans == float('inf') else ans

print(Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))

