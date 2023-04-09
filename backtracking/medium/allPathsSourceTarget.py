# https://leetcode.com/problems/all-paths-from-source-to-target/description/

def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    target = len(graph) - 1
    # the path starts from the first node
    path = [0]
    ans = []

    def backtrack(node: int, path: list[int]) -> None:
        # 3. every time backtrack runs check the expression below
        if node == target:
            ans.append(list(path))
            return

        # 2. for all of the neighs in graph we create a path, store prev node, then remove it from the top
        for neig in graph[node]:
            path.append(neig)
            backtrack(neig, path)
            path.pop()

    # 1. start from the first node
    backtrack(0, path)

    return ans


print(allPathsSourceTarget([[1, 2], [3], [3], []]))  # [[0,1,3],[0,2,3]]
# [[0,1,3],[0,2,3]]
# [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
print(allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
