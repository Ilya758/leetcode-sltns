class Solution:
    def findFarmland(self, grid: list[list[int]]) -> list[list[int]]:
        toAdd = [0, 0, 0, 0]
        ans = []
        n, m = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        seen = set()

        def isValid(row, col):
            return 0 <= row < n and 0 <= col < m and grid[row][col]

        def dfs(row, col):
            nonlocal toAdd

            for dx, dy in dirs:
                x, y = row + dx, col + dy
                
                if isValid(x, y) and (x, y) not in seen:
                    toAdd[2] = max(toAdd[2], x)
                    toAdd[3] = max(toAdd[3], y)
                    seen.add((x, y))
                    dfs(x, y)
        
        for i in range(n):
            for j in range(m):
                if isValid(i, j) and (i, j) not in seen:
                    toAdd = [i, j, i, j]
                    seen.add((i, j))
                    dfs(i, j)
                    ans.append(toAdd) 

        return ans
    
print(Solution().findFarmland(land = [[1,0,0],[0,1,1],[0,1,1]])) # [[0,0,0,0],[1,1,2,2]]