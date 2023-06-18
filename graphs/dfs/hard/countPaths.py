class Solution:
    ans = 0

    def countPaths(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cache = {}
        mod = 10 ** 9 + 7

        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n

        def dfs(row, col):
            if (row, col) in cache:
                return cache[(row, col)]

            count = 1

            for dx, dy in dirs:
                x, y = row + dy, col + dx

                if isValid(x, y) and grid[x][y] > grid[row][col]:
                    count += dfs(x, y)

            cache[(row, col)] = count
            return cache[(row, col)]

        for i in range(m):
            for j in range(n):
                self.ans += dfs(i, j)

        return self.ans % mod


print(Solution().countPaths(grid=[[1, 1], [3, 4]]))  # 8
