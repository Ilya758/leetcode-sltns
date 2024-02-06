import collections


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = collections.defaultdict(set)
        res = [0] * n
        count = [1] * n

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]

        def dfs2(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] - 2 * count[child] + n
                    dfs2(child, node)

        dfs()
        dfs2()

        return res

print(Solution().sumOfDistancesInTree(n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]])) # [8,12,6,10,10,10]