# https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isValid(row: int, col: int) -> bool:
            return 0 <= row < m and 0 <= col < n

        def check(effort) -> bool:
            stack = [(0, 0)]
            seen = {(0, 0)}

            while stack:
                row, col = stack.pop()

                if (row, col) == (m - 1, n - 1):
                    return True

                for dx, dy in dirs:
                    x, y = row + dy, col + dx

                    if isValid(x, y) and (x, y) not in seen:
                        if abs(heights[x][y] - heights[row][col]) <= effort:
                            stack.append((x, y))
                            seen.add((x, y))

            return False

        left = 0
        right = max(max(row) for row in heights)

        while left <= right:
            mid = (left + right) // 2

            # for binary search we check, if the effort is enough to
            # gotta the bottom right corner
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


print(Solution().minimumEffortPath(
    heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))  # 2
