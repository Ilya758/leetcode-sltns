from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        q = deque([i for i in range(n) if degree[i] == 1])
        remain = n

        while remain > 2:
            m = len(q)
            remain -= m

            for _ in range(m):
                node = q.popleft()

                for nei in graph[node]:
                    degree[nei] -= 1

                    if degree[nei] == 1:
                        q.append(nei)

        return q
    
print(Solution().findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]])) # [3,4]