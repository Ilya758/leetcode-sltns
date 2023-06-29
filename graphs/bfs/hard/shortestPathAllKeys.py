# https://leetcode.com/problems/shortest-path-to-get-all-keys/description/

from collections import defaultdict, deque


class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        startX, startY = None, None
        m = len(grid)
        n = len(grid[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        count = 0

        for row in range(m):
            for col in range(n):
                cell = grid[row][col]

                if cell == '@':
                    startX, startY = row, col
                elif cell in 'ABCDEF':
                    count += 1

        seen = defaultdict(set)
        seen[''].add((startX, startY))

        def isValid(row, col):
            if not (0 <= row < m and 0 <= col < n):
                return False

            cell = grid[row][col]

            if cell in 'ABCDEF':
                return cell.lower() in keys

            return cell != '#'

        q = deque([(startX, startY, 0, '')])

        while q:
            row, col, steps, keys = q.popleft()
            cell = grid[row][col]

            if cell in 'abcdef':
                if cell not in keys:
                    keys += cell
                    seen[keys].add((row, col))

                    if len(keys) == count:
                        return steps

            for dx, dy in dirs:
                x, y = row + dy, col + dx

                if isValid(x, y) and (x, y) not in seen[keys]:
                    seen[keys].add((x, y))
                    q.append((x, y, steps + 1, keys))

        return -1


print(Solution().shortestPathAllKeys(grid=["@.a..", "###.#", "b.A.B"]))  # 8
print(Solution().shortestPathAllKeys(grid=["@..aA", "..B#.", "....b"]))  # 6
print(Solution().shortestPathAllKeys(["@Aa"]))  # -1
print(Solution().shortestPathAllKeys(["@...a", ".###A", "b.BCc"]))  # 10
