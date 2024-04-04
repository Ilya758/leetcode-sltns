from collections import defaultdict


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        cache = defaultdict(int)

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[i])):
                    matrix[i][j] ^= 1
            
            cache[tuple(matrix[i])] += 1

        return max(cache.values())

print(Solution().maxEqualRowsAfterFlips(matrix = [[0,0,0],[0,0,1],[1,1,0]])) # 2