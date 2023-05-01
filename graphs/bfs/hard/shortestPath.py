# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

from collections import deque


def shortestPath(grid: list[list[int]], k: int) -> int:
    def isValid(row, col):
        return 0 <= row < m and 0 <= col < n

    m = len(grid)
    n = len(grid[0])
    # 1. first we initialize a queue
    # that stores x,y,remain possible obstacles count and steps
    q = deque([(0, 0, k, 0)])
    seen = {(0, 0, k)}
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q:
        row, col, remain, steps = q.popleft()

        # if the cell is in the right corner, then return
        # number of steps
        if (row, col) == (m - 1, n - 1):
            return steps

        # 2. otherwise go thru the neigbours
        for dx, dy in dirs:
            x, y = row + dx, col + dy

            # 3. check if we're within matrix at each possible step
            if isValid(x, y):
                # 4.1 if the cell is empty
                if (grid[x][y] == 0):
                    if (x, y, remain) not in seen:
                        # we can go further
                        seen.add((x, y, remain))
                        q.append((x, y, remain, steps+1))
                # 4.2 if it's an obstacle and we can pass it
                elif remain and (x, y, remain - 1) not in seen:
                    # then go to the next level
                    seen.add((x, y, remain - 1))
                    q.append((x, y, remain - 1, steps+1))

    return -1


print(shortestPath(grid=[[0, 0, 0], [1, 1, 0], [
      0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1))  # 6
