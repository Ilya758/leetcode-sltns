from heapq import *


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def isValid(row, col):
            return 0 <= row < n and 0 <= col < m

        dirs = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0),
        }

        heap = [(0, 0, 0)]
        heapify(heap)
        seen = set()

        while heap:
            steps, row, col = heappop(heap)

            if (row, col) in seen:
                continue
            
            seen.add((row, col))

            if (row, col) == (n - 1, m - 1):
                return steps

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = row + dx, col + dy
                
                if isValid(x, y):
                    extraStep = int(dirs[grid[row][col]] != (dx, dy))
                    heappush(heap, (steps + extraStep, x, y))


print(Solution().minCost([[1,1,3],[3,2,2],[1,1,4]])) # 0
                 