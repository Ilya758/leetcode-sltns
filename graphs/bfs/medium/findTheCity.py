from collections import defaultdict
import heapq

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], d: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def getCitiesCount(source):
            distances = [float('inf')] * n
            distances[source] = 0
            heap = [(0, source)]

            while heap:
                curDist, node = heapq.heappop(heap)

                if curDist != distances[node]:
                    continue

                for nei, w in graph[node]:
                    dist = curDist + w

                    if dist < distances[nei]:
                        distances[nei] = curDist + w
                        heapq.heappush(heap, (dist, nei))

            return len([x for x in distances if x <= d])

        count = float('inf')
        ans = -1

        for i in range(n):
            nei = getCitiesCount(i)

            if nei <= count:
                count = nei
                ans = i

        return ans


print(Solution().findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4)) # 3