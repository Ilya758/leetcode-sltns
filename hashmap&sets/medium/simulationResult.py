from collections import deque


class Solution:
    def simulationResult(self, windows: list[int], queries: list[int]) -> list[int]:
        q = deque(windows)

        for v in queries:
            q.appendleft(v)

        seen = set()
        ans = []

        for v in q:
            if v not in seen:
                seen.add(v)
                ans.append(v)

        return ans

print(Solution().simulationResult(windows = [1,2,3], queries = [3,3,2])) # [2,3,1]