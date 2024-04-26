from functools import cache


class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        ans = float('inf')
        n = len(grid)

        @cache
        def dp(row, col):
            if row == n - 1:
                return grid[row][col]

            cur = float('inf')

            for nxtCol in range(n):
                if nxtCol != col:
                    cur = min(cur, grid[row][col] + dp(row + 1, nxtCol))

            return cur

        for i in range(n):
            ans = min(ans, dp(0, i))

        return ans
    
print(Solution().minFallingPathSum(grid = [[1,2,3],[4,5,6],[7,8,9]])) # 13