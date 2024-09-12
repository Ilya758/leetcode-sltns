from collections import defaultdict


class Solution:
    def findSmallestRegion(self, regions: list[list[str]], A: str, B: str) -> str:
        graph = defaultdict(str)

        for r in regions:
            for i in range(1, len(r)):
                graph[r[i]] = r[0]

        seen = set()

        while A in graph:
            seen.add(A)
            A = graph[A]

        seen.add(A)

        while B not in seen:
            B = graph[B]

        return B

print(Solution().findSmallestRegion(regions =
[["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]], A = "Quebec", B = "New York")) # North America