# https://leetcode.com/problems/find-eventual-safe-states/description/

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        self.ans = set()
        terminalNodes = []
        n = len(graph)
        cache = dict()

        for i in range(n):
            if not len(graph[i]):
                terminalNodes.append(i)

        def dfs(node, seen):
            if node in terminalNodes:
                self.ans.add(node)
                return True

            validPathCount = 0

            for neig in graph[node]:
                if neig not in seen:
                    seen.add(neig)

                    if neig not in cache:
                        cache[neig] = int(dfs(neig, seen))

                    validPathCount += cache[neig]
                    seen.remove(neig)

            if validPathCount == len(graph[node]):
                self.ans.add(node)
                return True

            return False

        for i in range(n):
            dfs(i, set())

        return sorted(list(self.ans))


print(Solution().eventualSafeNodes(
    [[], [0, 2, 3, 4], [3], [4], []]))  # [0,1,2,3,4]
print(Solution().eventualSafeNodes(
    graph=[[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))  # [4]
print(Solution().eventualSafeNodes(
    graph=[[1, 2], [2, 3], [5], [0], [5], [], []]))  # [2, 4, 5, 6]
