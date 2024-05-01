from heapq import *


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def isValid(row, col):
            return 0 <= row < n and 0 <= col < n

        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}

        while heap:
            steps, row, col = heappop(heap)

            if row == col == n - 1:
                return steps

            for dx, dy in dirs:
                x, y = row + dx, col + dy

                if isValid(x, y) and (x, y) not in seen:
                    seen.add((x, y))
                    heappush(heap, (max(steps, grid[x][y]), x, y))

print(Solution().swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])) # 16