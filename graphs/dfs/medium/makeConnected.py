class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if n - 1 > len(connections):
            return -1

        adjList = [[] for _ in range(n)]
        
        for u, v in connections: 
            adjList[u].append(v)
            adjList[v].append(u)
        
        ans = -1
        seen = set()

        def dfs(node):
            for n in adjList[node]:
                if n not in seen:
                    seen.add(n)
                    dfs(n)

        for i in range(n):
            if i not in seen:
                seen.add(i)
                ans += 1
                dfs(i)

        return ans


print(Solution().makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]])) # 2