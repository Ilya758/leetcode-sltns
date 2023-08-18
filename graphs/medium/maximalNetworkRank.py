from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        graph = defaultdict(list)

        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        ans = 0

        # although bruteforce isn't efficient,
        # this approach is quite common,
        # but in cases with large data it causes at least TLE
        for i in range(n):
            for j in range(n):
                if i != j:
                    cur = len(graph[i]) + len(graph[j]) - int(i in graph[j])

                    if (cur > ans):
                        ans = max(ans, cur)

        return ans


print(Solution().maximalNetworkRank(n=8, roads=[
      [0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]))  # 5
