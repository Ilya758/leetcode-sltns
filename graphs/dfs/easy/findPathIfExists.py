from collections import defaultdict


def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    graph = defaultdict(list)
    seen = set()

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    def dfs(node: int) -> bool:
        if destination == node:
            return True

        if node not in seen:
            seen.add(node)
            for neig in graph[node]:
                if dfs(neig):
                    return True

        return False

    return dfs(source)


print(validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]],
      source=0, destination=2))  # true
print(validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [
    5, 4], [4, 3]], source=0, destination=5))  # false
