class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        def occupied(row, col):
            return 0 <= row < n and 0 <= col < m and grid[row][col]

        n, m = len(grid), len(grid[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    cur = 0

                    for dx, dy in dirs:
                        x, y = i + dx, j + dy

                        if not occupied(x, y):
                            cur += 1

                    ans += cur

        return ans


print(Solution().islandPerimeter([[1, 1]])) # 6