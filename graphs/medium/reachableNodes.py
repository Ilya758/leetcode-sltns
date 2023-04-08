from collections import defaultdict

#  https://leetcode.com/problems/reachable-nodes-with-restrictions/description/


def reachableNodes(n: int, edges: list[list[int]], restricted: list[int]) -> int:
    # this set is for optimization
    restr = set(restricted)
    seen = set()
    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node: int) -> int:
        seen.add(node)
        ans = 1

        for neig in graph[node]:
            if not neig in seen and not neig in restr:
                ans += dfs(neig)

        return ans

    return dfs(0)


print(reachableNodes(n=7, edges=[[0, 1], [1, 2], [3, 1], [
      4, 0], [0, 5], [5, 6]], restricted=[4, 5]))  # 4
print(reachableNodes(n=7, edges=[[0, 1], [0, 2], [0, 5], [
      0, 4], [3, 2], [6, 5]], restricted=[4, 2, 1]))  # 3
