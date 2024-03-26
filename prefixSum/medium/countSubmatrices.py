class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0

        for i in range(n):
            for j in range(m):
                if i:
                    grid[i][j] += grid[i - 1][j]
                if j:
                    grid[i][j] += grid[i][j - 1]
                
                if i and j:
                    grid[i][j] -= grid[i - 1][j - 1]

                if grid[i][j] <= k:
                    ans += 1

        return ans
    
print(Solution().countSubmatrices(grid = [[7,6,3],[6,6,1]], k = 18)) # 4