class Solution:
    def matrixBlockSum(self, mat, k):
        m, n = len(mat), len(mat[0])
        range_sum = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                range_sum[i+1][j+1] = mat[i][j] + range_sum[i+1][j] + range_sum[i][j+1] - range_sum[i][j]

        res = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                r1, c1, r2, c2 = max(0, i-k), max(0, j-k), min(m, i+k+1), min(n, j+k+1)
                res[i][j] = range_sum[r2][c2] - range_sum[r2][c1] - range_sum[r1][c2] + range_sum[r1][c1]

        return res

print(Solution().matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
)) # [[12,21,16],[27,45,33],[24,39,28]]