# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left = 0
        right = m * n - 1
        mid = 0

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            cell = matrix[row][col]
            print(mid, row, col, cell)

            if cell == target:
                return True
            elif cell < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


print(Solution().searchMatrix(matrix=[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]],
    target=3))  # True
