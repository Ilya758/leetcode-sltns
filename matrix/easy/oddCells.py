class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        for r, c in indices:
            for i in range(n):
                matrix[r][i] += 1

            for i in range(m):
                matrix[i][c] += 1

        ans = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] & 1:
                    ans += 1

        return ans
    
print(Solution().oddCells(2, 3, [[0,1],[1,1]]))