class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> list[list[int]]:
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        grid = [[-1] * n for _ in range(m)]
        grid[r][c] = 0

        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == -1

        def dfs(row, col, idx):
            if idx == m * n:
                return True

            for dx, dy in moves:
                x, y = row + dx, col + dy

                if isValid(x, y):
                    grid[x][y] = idx

                    if dfs(x, y, idx + 1):
                        return True

                    grid[x][y] = -1

            return False

        dfs(r, c, 1)

        return grid
    
print(Solution().tourOfKnight(m = 3, n = 4, r = 0, c = 0)) # [[0,3,6,9],[11,8,1,4],[2,5,10,7]]