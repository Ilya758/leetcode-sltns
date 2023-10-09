class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        seen = set()
        n, m = len(grid), len(grid[0])
        l = n * m
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def isValid(i, j):
            return 0 <= i < n and 0 <= j < m

        def bt(row, col):
            if len(seen) == l and grid[row][col] == 2:
                return 1

            result = 0

            for dx, dy in dirs:
                x, y = row + dx, col + dy
                key = (x, y)

                if isValid(x, y) and key not in seen and grid[row][col] != -1:
                    seen.add(key)
                    result += bt(x, y)
                    seen.remove(key)

            return result

        start = None

        for i in range(n):
            for j in range(m):
                match grid[i][j]:
                    case 1:
                        start = [i, j]
                        seen.add((i, j))

                    case -1:
                        l -=1

        return bt(start[0], start[1])

print(Solution().uniquePathsIII(grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]])) # 2