class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        n, m = len(grid), len(grid[0])
        ans = [[0] * m for _ in range(n)]

        for row in range(n):
            count = grid[row].count(1)
            ans[row] = [count - (m - count)] * m

        for col in range(m):
            count = 0

            for row in range(n):
                if grid[row][col]:
                    count += 1

            for row in range(n):
                ans[row][col] += count - (n - count)

        return ans
    
print(Solution().onesMinusZeros(grid = [[0,1,1],[1,0,1],[0,0,1]])) #  [[0,0,4],[0,0,4],[-2,-2,2]] 