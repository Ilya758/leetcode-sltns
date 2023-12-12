class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        n, m = len(mat), len(mat[0])

        if n * m != r * c:
            return mat

        ans = [[0] * c for _ in range(r)]

        for i in range(n):
            for j in range(m):
                pos = i * m + j
                ans[pos // c][pos % c] = mat[i][j] 

        return ans
    
print(Solution().matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4)) # [[1,2,3,4]]
print(Solution().matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4)) # [[1,2],[3,4]]