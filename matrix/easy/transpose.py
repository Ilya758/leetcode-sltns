class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        n, m = len(matrix), len(matrix[0])
        ans = [[0] * n for _ in range(m)]

        for row in range(n):
            for col in range(m):
                ans[col][row] = matrix[row][col]

        return ans
    
print(Solution().transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]])) # [[1,4,7],[2,5,8],[3,6,9]]