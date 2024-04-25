from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        graph = defaultdict(list)
        seen = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            res = 0

            for nei in graph[node]:
                if (node, nei) not in seen and (nei, node) not in seen:
                    seen.add((node, nei))
                    res += dfs(nei)
            
            if (hasApple[node] and not res) or res:
                return res + 1
            
            return res
            
        return max(dfs(0) * 2 - 2, 0)

print(Solution().minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False])) # 6