from functools import cache


class Solution:
    def minPathCost(self, grid: list[list[int]], moveCost: list[list[int]]) -> int:
        m = len(grid[0])

        @cache
        def dp(i, j):
            cur = grid[i][j]

            if i == len(grid) - 1:
                return grid[i][j]

            return min(cur + moveCost[cur][k] + dp(i + 1, k) for k in range(m))

        return min(dp(0, j) for j in range(m))
    
print(Solution().minPathCost(grid = [[5,3],[4,0],[2,1]], moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]])) # 17