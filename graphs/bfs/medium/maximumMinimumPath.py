from heapq import *


class Solution:
    def maximumMinimumPath(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])       
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        seen = {(0, 0)}
        q = [(-grid[0][0], 0, 0)]
        dist = [[float('-inf')] * m for _ in range(n)]
        dist[0][0] = -grid[0][0]

        def isValid(row, col):
            return 0 <= row < n and 0 <= col < m and (row, col) not in seen

        while q:
            cost, row, col = heappop(q)

            if cost != dist[row][col]:
                continue

            for dx, dy in dirs:
                x, y = row + dx, col + dy

                if isValid(x, y):
                    nxt = max(cost, -grid[x][y])
                    
                    if nxt > dist[x][y]: 
                        seen.add((x, y))
                        heappush(q, (nxt, x, y))
                        dist[x][y] = nxt

        return -dist[-1][-1]
    
print(Solution().maximumMinimumPath(grid = [[5,4,5],[1,2,6],[7,4,6]])) # 4