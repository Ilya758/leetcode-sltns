# https://leetcode.com/problems/is-graph-bipartite/

class Solution(object):
    def isBipartite(self, graph):
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True


print(Solution().isBipartite(graph=[
    [1, 2, 3],
    [0, 2],
    [0, 1, 3],
    [0, 2]]
))  # False
