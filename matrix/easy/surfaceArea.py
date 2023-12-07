class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def getVal(row, col):
            return grid[row][col] if 0 <= row < n and 0 <= col < n else 0

        for row in range(n):
            for col in range(m):
                for dx, dy in dirs:
                    x, y = dx + row, dy + col
                    ans += max(0, grid[row][col] - getVal(x, y))

                ans += 2 * int(grid[row][col] > 0)

        return ans
    
print(Solution().surfaceArea([[1,1,1],[1,0,1],[1,1,1]])) # 32