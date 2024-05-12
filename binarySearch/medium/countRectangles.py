from bisect import bisect_left
from collections import defaultdict


class Solution:
    def countRectangles(self, rectangles: list[list[int]], points: list[list[int]]) -> list[int]:
        rectangles.sort()
        length = defaultdict(list)

        for l, h in rectangles:
            length[h].append(l)

        ans = []

        for x, y in points:
            cur = 0

            for h in range(y, 101):
                cur += len(length[h]) - bisect_left(length[h], x)

            ans.append(cur)
    
        return ans

print(Solution().countRectangles(rectangles =
[[7,1],[2,6],[1,4],[5,2],[10,3],[2,4],[5,9]],
points =
[[10,3],[8,10],[2,3],[5,4],[8,5],[7,10],[6,6],[3,6]])) # [1, 0, 4, 1, 0, 0, 0, 1]