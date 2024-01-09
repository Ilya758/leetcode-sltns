class Solution:
    def differenceOfDistinctValues(self, grid: list[list[int]]) -> list[list[int]]:
        n, m = len(grid), len(grid[0])
        ans = [[0] * m for _ in range(n)]

        def isValid(row, col):
            return 0 <= row < n and 0 <= col < m

        for i in range(n):
            for j in range(m):
                left, right = set(), set()
                a, b = i, j

                while True:
                    a -= 1
                    b -= 1

                    if isValid(a, b):
                        left.add(grid[a][b])
                    else: 
                        break
                
                a, b = i, j

                while True:
                    a += 1
                    b += 1

                    if isValid(a, b):
                        right.add(grid[a][b])  
                    else: 
                        break
                        
                ans[i][j] = abs(len(right) - len(left))

        return ans
    
print(Solution().differenceOfDistinctValues([[1,2,3],[3,1,5],[3,2,1]]))