from collections import defaultdict

# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/


def countComponents(n: int, edges: list[list[int]]) -> int:
    graph = defaultdict(list)
    seen = set()

    for a, b in edges:
        # 1. the graph is undirected, so we'll build two-way connection
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node: int) -> None:
        # 3. once we've encountered 1 node as a part of a compound component (CC), we recursively
        # add other nodes of CC to the seen
        seen.add(node)

        for neig in graph[node]:
            if (neig not in seen):
                dfs(neig)

    ans = 0

    for i in range(n):
        if i not in seen:
            # 2. the point is to find one node, be sure that we haven't visited it before
            dfs(i)
            ans += 1

    return ans


print(countComponents(n=5, edges=[[0, 1], [1, 2], [3, 4]]))  # 2
print(countComponents(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]]))  # 1
