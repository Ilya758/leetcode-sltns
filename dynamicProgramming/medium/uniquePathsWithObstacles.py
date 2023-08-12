# https://leetcode.com/problems/unique-paths-ii/description/
from functools import cache


class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        @cache
        def dp(i, j):
            # 2. if the robot has reached the start point and
            # it's not an obstacle, this's a valid path
            if (i, j) == (0, 0) and not grid[i][j]:
                return 1

            # 3. otherwise check the boundary
            # and the obstacles at each step
            if i < 0 or j < 0 or grid[i][j]:
                return 0

            # 4. the equation is to led robot to follow
            # to top and to left
            return dp(i - 1, j) + dp(i, j - 1)

        # 1. start from the right bottom corner
        return dp(n - 1, m - 1)


print(Solution().uniquePathsWithObstacles(
    obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
