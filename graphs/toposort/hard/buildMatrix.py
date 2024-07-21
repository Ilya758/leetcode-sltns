from collections import defaultdict, deque


class Solution:
    def buildMatrix(self, k: int, R: list[list[int]], C: list[list[int]]) -> list[list[int]]:
        def topoSort(col):
            graph = defaultdict(list)
            indegree = [0] * (k + 1)

            for u, v in col:
                graph[u].append(v)
                indegree[v] += 1

            q = deque([i for i in range(1, k + 1) if not indegree[i]])
            n = k - len(q)
            res = []

            while q:
                node = q.popleft()
                res.append(node)

                for nei in graph[node]:
                    indegree[nei] -= 1

                    if not indegree[nei]:
                        q.append(nei)
                        
                        n -= 1

            return res if not n else []

        rows, cols = topoSort(R), topoSort(C)
        
        if not rows or not cols:
            return []
        
        ans = [[0] * k for _ in range(k)]

        for i in range(len(rows)):
            for j in range(len(cols)):
                if rows[i] == cols[j]:
                    ans[i][j] = rows[i]

        return ans

print(Solution().buildMatrix(k = 3, R = [[1,2],[3,2]], C = [[2,1],[3,2]])) # [[0, 0, 1], [3, 0, 0], [0, 2, 0]]