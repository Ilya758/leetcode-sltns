from collections import defaultdict


class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        cache = defaultdict(list)
        n, m = len(mat), len(mat[0])

        for row in range(n):
            for col in range(m):
                if row - col not in cache:
                    cache[row - col] = [mat[row][col]]
                else:
                    cache[row - col].append(mat[row][col])
        
        print(cache)
        for key in cache.keys():
            cache[key].sort(reverse=True)
            
        for row in range(n):
            for col in range(m):
                mat[row][col] = cache[row - col].pop()

        return mat
    
print(Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])) # [[1,1,1,1],[1,2,2,2],[1,2,3,3]]