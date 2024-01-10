from collections import defaultdict


class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        graph = defaultdict(list)
        vals = defaultdict(int)

        for e in employees:
            graph[e.id].extend(e.subordinates)
            vals[e.id] = e.importance

        def dfs(node):
            res = 0

            for nei in graph[node]:
                res += vals[nei] + dfs(nei)
        
            return res

        return vals[id] + dfs(id)