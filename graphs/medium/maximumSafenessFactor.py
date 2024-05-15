from collections import deque


class Solution:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        thieves = deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    thieves.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1

        while thieves:
            n = len(thieves)

            for _ in range(n):
                row, col = thieves.popleft()
                
                for dx, dy in self.dirs:
                    x, y = row + dx, col + dy
                    val = grid[row][col]
                    
                    if self.isValidCell(grid, x, y) and grid[x][y] == -1:
                        grid[x][y] = val + 1
                        thieves.append((x, y))
        
        left, right, res = 0, max(max(row) for row in grid), -1

        while left <= right:
            mid = (left + right) >> 1

            if self.isValidSafeness(grid, mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res
    
    def isValidCell(self, grid, i, j) -> bool:
        n = len(grid)
        return 0 <= i < n and 0 <= j < n

    def isValidSafeness(self, grid, min_safeness) -> bool:
        n = len(grid)

        if grid[0][0] < min_safeness or grid[n - 1][n - 1] < min_safeness:
            return False

        queue = deque([(0, 0)])
        seen = {(0, 0)}

        while queue:
            row, col = queue.popleft()

            if row == col == n - 1:
                return True

            for dx, dy in self.dirs:
                x, y = row + dx, col + dy

                if self.isValidCell(grid, x, y) and (x, y) not in seen and grid[x][y] >= min_safeness:
                    seen.add((x, y))
                    queue.append((x, y))

        return False
    
print(Solution().maximumSafenessFactor(grid =
[[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
)) # 2