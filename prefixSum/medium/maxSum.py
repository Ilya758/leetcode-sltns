class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        for i in range(m - 2):
            for j in range(1, n - 1):
               ans = max(ans,
                    grid[i][j - 1] + grid[i][j] + grid[i][j + 1]
                    + grid[i + 1][j]
                    + grid[i + 2][j - 1] + grid[i + 2][j] + grid[i + 2][j + 1]
                ) 

        return ans
    
print(Solution().maxSum(grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
)) # 30