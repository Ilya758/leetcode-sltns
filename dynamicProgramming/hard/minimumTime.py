from collections import defaultdict
from functools import cache


class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        graph = defaultdict(list)

        for a, b in relations:
            graph[a - 1].append(b - 1)

        @cache
        def dp(node):
            if not graph[node]: return time[node]

            ans = 0

            for nei in graph[node]:
                ans = max(ans, dp(nei))
            
            return time[node] + ans

        ans = 0

        for node in range(n):
            ans = max(ans, dp(node))

        return ans

print(Solution().minimumTime(n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5])) # 12