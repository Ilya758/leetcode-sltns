# https://leetcode.com/problems/unique-paths/

from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(row, col):
            if (row, col) == (0, 0):
                return 1

            ways = 0

            if row:
                ways += dp(row - 1, col)
            if col:
                ways += dp(row, col - 1)

            return ways

        return dp(m - 1, n - 1)


print(Solution().uniquePaths(m=3, n=7))  # 28
