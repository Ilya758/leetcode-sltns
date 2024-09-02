class Solution:
    def candyCrush(self, grid: list[list[int]]) -> list[list[int]]:
        n, m = len(grid), len(grid[0])

        def find():
            res = set()

            for i in range(1, n - 1):
                for j in range(m):
                    if grid[i][j] and grid[i - 1][j] == grid[i][j] == grid[i + 1][j]:
                        res.add((i - 1, j))
                        res.add((i, j))
                        res.add((i + 1, j))

            for i in range(n):
                for j in range(1, m - 1):
                    if grid[i][j] and grid[i][j - 1] == grid[i][j] == grid[i][j + 1]:
                        res.add((i, j - 1))
                        res.add((i, j))
                        res.add((i, j + 1))

            return res

        def crush():
            for i, j in toCrush:
                grid[i][j] = 0

        def drop():
            for j in range(m):
                idx = -1
                
                for i in range(n - 1, -1, -1):
                    if not grid[i][j]:
                        idx = max(idx, i)
                    elif idx >= 0:
                        grid[i][j], grid[idx][j] = grid[idx][j], grid[i][j]
                        idx -= 1 

        toCrush = find()

        while toCrush:
            crush()
            drop()
            toCrush = find()

        return grid
    
print(Solution().candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,1,714],[810,1,2,2,1],[1,1,2,2,2],[4,1,4,4,1014]]))