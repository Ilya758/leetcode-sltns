class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        rowFlips, colFlips = 0, 0
        n, m = len(grid), len(grid[0])
        
        for i in range(n):
            l, r = 0, m - 1

            while l < r:
                rowFlips += grid[i][l] ^ grid[i][r]
                l += 1
                r -= 1
        
        for j in range(m):
            l, r = 0, n - 1

            while l < r:
                colFlips += grid[l][j] ^ grid[r][j]
                l += 1
                r -= 1
        
        return min(rowFlips, colFlips)

print(Solution().minFlips(grid = [[1,0,0],[0,0,0],[0,0,1]])) # 2