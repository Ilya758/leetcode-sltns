class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        n, m = len(rowSum), len(colSum)
        ans = [[0] * m for _ in range(n)]

        for row in range(n):
            for col in range(m):
                curMin = min(rowSum[row], colSum[col])
                ans[row][col] = curMin
                rowSum[row] -= curMin
                colSum[col] -= curMin

        return ans
    
print(Solution().restoreMatrix(rowSum = [3,8], colSum = [4,7])) # [[3,0], [1,7]]