# https://leetcode.com/problems/max-area-of-island/description/

def maxAreaOfIsland(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    ans = 0
    visited = [[False for _ in range(n)] for _ in range(m)]
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def isValid(row: int, col: int) -> bool:
        return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

    def dfs(row: int, col: int) -> int:
        if not isValid(row, col) or visited[row][col]:
            return 0

        visited[row][col] = True
        cur = 1

        # 2. for every possible directions, find the land cells
        for dx, dy in dirs:
            cur += dfs(row + dx, col + dy)

        return cur

    for row in range(m):
        for col in range(n):
            if grid[row][col] and not visited[row][col]:
                # 1. once we've found land, we need find other land cells
                ans = max(ans, dfs(row, col))

    return ans


print(maxAreaOfIsland(grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))  # 6
