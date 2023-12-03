class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        for row in range(n):
            if not grid[row][0]:
                for col in range(m):
                    grid[row][col] ^= 1

        for col in range(m):
            count = 0

            for row in range(n):
                if grid[row][col]:
                    count += 1

            if count < n / 2:
                for row in range(n):
                    grid[row][col] ^= 1

        return sum(int(''.join(map(str, row)), 2) for row in grid)
    
print(Solution().matrixScore(grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]))