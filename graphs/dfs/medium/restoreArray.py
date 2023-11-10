from collections import defaultdict


class Solution:
    def restoreArray(self, adj: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        ans = []
        seen = set()

        for a, b in adj:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            for neig in graph[node]:
                if neig not in seen: 
                    seen.add(neig)
                    ans.append(neig)
                    dfs(neig)

        for node in graph:
            if len(graph[node]) == 1:
                ans.append(node)
                seen.add(node)
                dfs(node)
                break        
        
        return ans
    
print(Solution().restoreArray([[2,1],[3,4],[3,2]])) # [1,2,3,4]