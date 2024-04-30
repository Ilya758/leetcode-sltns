class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        indegree = [0 for _ in range(n)]

        for _, b in edges:
            indegree[b] += 1

        if indegree.count(0) > 1:
            return -1

        return indegree.index(0)

print(Solution().findChampion(n = 3, edges = [[0,1],[1,2]])) # 0