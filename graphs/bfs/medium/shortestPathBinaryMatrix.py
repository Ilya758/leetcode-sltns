from collections import deque


def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:
    if grid[0][0]:
        return -1

    def isValid(row: int, col: int) -> bool:
        return 0 <= row < n and 0 <= col < n and not grid[row][col]

    n = len(grid)
    seen = {(0, 0)}
    q = deque([(0, 0, 1)])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (-1, -1), (1, -1), (-1, 1)]

    while q:
        row, col, steps = q.popleft()

        if (row, col) == (n - 1, n - 1):
            print(seen)
            return steps

        for dx, dy in dirs:
            x, y = row + dx, col + dy

            if isValid(x, y) and (x, y) not in seen:
                seen.add((x, y))
                q.append((x, y, steps + 1))

    return -1


print(shortestPathBinaryMatrix(grid=[[0, 1], [1, 0]]))  # 2
print(shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]]))  # 4
print(shortestPathBinaryMatrix(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 0]]))  # -1
