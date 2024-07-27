from collections import defaultdict
from heapq import *


class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        graph = defaultdict(list)
        cache = defaultdict(int)
        dist = defaultdict(lambda: float('inf'))

        for u, v, w in zip(original, changed, cost):
            graph[u].append((v, w))

        def find(start, end):
            heap = [[0, start]]
            dist[start] = 0

            while heap:
                cost, node = heappop(heap)

                if cost != dist[node]:
                    continue

                if node == end:
                    return cost

                for nei, w in graph[node]:
                    x = cost + w

                    if x < dist[nei]:
                        dist[nei] = x
                        heappush(heap, [x, nei])

            return float('inf')

        ans = 0

        for u, v in zip(source, target):
            w = cache[(u, v)] if (u, v) in cache else find(u, v)

            if w == float('inf'):
                return -1

            ans += w
            cache[(u, v)] = w
            dist.clear() 

        return ans


print(Solution().minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
)) # 28