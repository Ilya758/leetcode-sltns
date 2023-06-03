# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

from collections import defaultdict


class Solution:
    ans = 0

    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        graph = defaultdict(list)

        for id, man in enumerate(manager):
            if man != -1:
                graph[man].append(id)

        def dfs(node, cur):
            if node not in graph:
                self.ans = max(self.ans, cur)
                return

            for nei in graph[node]:
                dfs(nei, cur + informTime[nei])

        dfs(headID, informTime[headID])

        return self.ans


print(Solution().numOfMinutes(n=6, headID=2, manager=[
      2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]))  # 1
