# https://leetcode.com/problems/number-of-enclaves/description/

def numEnclaves(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    seen = [[False for _ in range(n)] for _ in range(m)]
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    ans = 0

    def dfs(row: int, col: int) -> None:
        # if a current cell is out of boundaries, or if it's not a ground or we've already visited this cell
        if (row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0 or seen[row][col]):
            return

        seen[row][col] = True

        # for every right-left-bottom-top direction we visit all of the possible neighbors
        for dx, dy in dirs:
            dfs(row + dx, col + dy)

        return

    for row in range(m):
        # perform dfs with the first
        if grid[row][0] and not seen[row][0]:
            dfs(row, 0)
        # and the last column
        if grid[row][n - 1] and not seen[row][n - 1]:
            dfs(row, n - 1)

    for col in range(n):
        # the same, but with the first and with the last rows
        if grid[0][col] and not seen[0][col]:
            dfs(0, col)

        if grid[m - 1][col] and not seen[m - 1][col]:
            dfs(m - 1, col)

    for row in range(m):
        for col in range(n):
            if grid[row][col] and not seen[row][col]:
                ans += 1

    return ans


print(numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0],
      [0, 1, 1, 0], [0, 0, 0, 0]]))  # == 3
print(numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0],
      [0, 0, 1, 0], [0, 0, 0, 0]]))  # == 0
