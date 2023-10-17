class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0] * col for _ in range(row)]

        for i in range(row):
            dp[i][0] = matrix[i][0]

        for i in range(col):
            dp[0][i] = matrix[0][i]

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        
        return sum([sum(row) for row in dp])
    
print(Solution().countSquares(matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
)) # 15