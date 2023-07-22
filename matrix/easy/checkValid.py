# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            rowCache = [False] * n
            colCache = [False] * n

            for j in range(n):
                rowCache[matrix[i][j] - 1] = True
                colCache[matrix[j][i] - 1] = True

            if not all(rowCache) or not all(colCache):
                return False

        return True


print(Solution().checkValid(matrix=[[1, 2, 3], [3, 1, 2], [2, 3, 1]]))  # True
print(Solution().checkValid(matrix=[[1, 1, 1], [1, 2, 3], [1, 2, 3]]))  # True
