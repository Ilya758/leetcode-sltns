from collections import defaultdict, deque


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        cache = defaultdict(list)
        n = len(graph)
        indegree = [0] * n
        ans = [False] * n

        for u, neis in enumerate(graph):
            for nei in neis:
                cache[nei].append(u)
                indegree[u] += 1

        q = deque([i for i in range(n) if indegree[i] == 0])

        while q:
            node = q.popleft()
            ans[node] = True

            for nei in cache[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return [i for i in range(n) if ans[i]]

print(Solution().eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]])) # [2,4,5,6]