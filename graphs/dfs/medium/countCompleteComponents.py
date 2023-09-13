from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        ans = 0
        
        def dfs(node, vertices):
            for neib in graph[node]:
                if neib not in seen:
                    seen.add(neib)
                    vertices.append(neib)
                    dfs(neib, vertices) 

        def isCompleted(vertices):
            edgesCount = 0
            nodesCount = len(vertices)

            for v in vertices:
                edgesCount += len(graph[v])

            return edgesCount == nodesCount * (nodesCount - 1)

        for i in range(n):
            if i not in seen:
                vertices = []
                dfs(i, vertices)

                if isCompleted(vertices):
                    ans += 1

        return ans
    
print(Solution().countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]])) # 3