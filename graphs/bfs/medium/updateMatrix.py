# https://leetcode.com/problems/01-matrix/

from collections import deque


def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    m = len(mat)
    n = len(mat[0])
    q = deque()
    seen = set()
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def isValid(row: int, col: int) -> bool:
        return 0 <= row < m and 0 <= col < n

    # 1. first we traverse all of the matrix to find zeros,
    # and there'll be starting points
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                q.append((i, j, 1))
                seen.add((i, j))

    while q:
        row, col, steps = q.popleft()

        for dx, dy in dirs:
            x, y = row + dx, col + dy

            # 2. once we've encountered new cell, that is a 1
            if isValid(x, y) and (x, y) not in seen:
                # 3. we update the matrix
                seen.add((x, y))
                mat[x][y] = steps
                # 4. by including steps for the next level
                q.append((x, y, steps+1))

    return mat


print(updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
# [[0,0,0],[0,1,0],[1,2,1]]
