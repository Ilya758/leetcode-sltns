# https://leetcode.com/problems/evaluate-division/description/

from collections import defaultdict


def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    # 3. perform query calculation
    def calcQuery(a: str, b: str) -> int:
        if a not in graph:
            return -1

        # 4. create seen + stack with varA / varB == ratio
        seen = {a}
        stack = [(a, 1)]

        while stack:
            node, ratio = stack.pop()

            if node == b:
                return ratio

            for neigh in graph[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    stack.append((neigh, ratio * graph[node][neigh]))

        return -1

    # 1. build a graph
    graph = defaultdict(dict)

    for i in range(len(equations)):
        a, b = equations[i]
        graph[a][b] = values[i]
        graph[b][a] = 1 / values[i]

    ans = []

    # 2. traverse by queries
    for a, b in queries:
        ans.append(calcQuery(a, b))

    return ans


print(calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0], queries=[["a", "c"], [
      "b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))  # [6.00000,0.50000,-1.00000,1.00000,-1.00000]
print(calcEquation(equations=[["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0], queries=[
      ["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))  # [3.75000,0.40000,5.00000,0.20000]
