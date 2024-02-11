class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cache = [[[-1] * m for _ in range(m)] for _ in range(n)]

        def dp(i, j, k):
            if i == n:
                return 0
            if cache[i][j][k] != -1:
                return cache[i][j][k]

            cherries = grid[i][j]

            if j != k:
                cherries += grid[i][k]

            res = 0

            for dj in [-1, 0, 1]:
                for dk in [-1, 0, 1]:
                    nj, nk = j + dj, k + dk

                    if 0 <= nj < m and 0 <= nk < m:
                        res = max(res, dp(i + 1, nj, nk))

            cache[i][j][k] = cherries + res

            return cache[i][j][k]

        return dp(0, 0, m - 1)

print(Solution().cherryPickup([[2,2], [2,2]])) # 4