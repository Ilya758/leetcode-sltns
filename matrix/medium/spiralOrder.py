def spiralOrder(matrix: list[list[int]]) -> list[int]:
    ans = []
    row = 0
    col = 0
    m = len(matrix)
    n = len(matrix[0])
    seen = set()
    dirs = {
        "U": (-1, 0, "R"),
        "D": (1, 0, "L"),
        "R": (0, 1, "D"),
        "L": (0, -1, "U"),
    }
    dir = 'R'

    def isValid(row: int, col: int) -> bool:
        return 0 <= row < m and 0 <= col < n

    while len(seen) != m * n:
        seen.add((row, col))
        ans.append(matrix[row][col])
        dx, dy, d = dirs[dir]
        x, y = row + dx, col + dy

        if not isValid(x, y) or (x, y) in seen:
            dir = d
            dx, dy, _ = dirs[dir]

        row, col = row + dx, col + dy

    return ans


# [1,2,3,6,9,8,7,4,5]
print(spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
