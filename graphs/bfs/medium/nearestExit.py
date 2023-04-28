# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/

from collections import deque


def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    m = len(maze)
    n = len(maze[0])
    [r, c] = entrance

    # initialize a deque as an efficient way to perform shift operation from the left side
    q = deque([(r, c, 0)])
    seen = {(r, c)}
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

    # the point to use this is for cases, when we will start from the border
    def isValid(row: int, col: int) -> bool:
        return 0 <= row < m and 0 <= col < n

    def isExit(row: int, col: int) -> bool:
        return (row == 0 or row == m - 1) or (col == 0 or col == n - 1)

    while q:
        row, col, steps = q.popleft()

        # the idea behind this is to check if we're at the border and current cell
        # is not a start position
        if (isExit(row, col) and (row, col) != (r, c)):
            return steps

        for dx, dy in dirs:
            x = row + dx
            y = col + dy

            if isValid(x, y) and maze[x][y] == '.' and (x, y) not in seen:
                seen.add((x, y))
                q.append((x, y, steps + 1))

    return -1


print(nearestExit(maze=[["+", "+", ".", "+"], [".", ".",
      ".", "+"], ["+", "+", "+", "."]], entrance=[1, 2]))  # 1
print(nearestExit(maze=[["+", "+", "+"], [".", ".", "."],
      ["+", "+", "+"]], entrance=[1, 0]))  # 2
