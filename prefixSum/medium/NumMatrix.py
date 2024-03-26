class NumMatrix:
    def __init__(self, A: list[list[int]]):
        n, m = len(A), len(A[0])

        for i in range(n):
            for j in range(m):
                if i:
                    A[i][j] += A[i - 1][j]
                if j:
                    A[i][j] += A[i][j - 1]
                if i and j:
                    A[i][j] -= A[i - 1][j - 1]

        self.A = A

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.A[row2][col2]

        if row1 > 0:
            res -= self.A[row1 - 1][col2]
        if col1 > 0:
            res -= self.A[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            res += self.A[row1 - 1][col1 - 1]
            
        return res
