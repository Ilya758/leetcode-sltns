from collections import defaultdict


class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        cache = defaultdict(int)
        n = len(mat)

        for row in mat:
            for num in row:
                cache[num] += 1

        ans = float('inf')

        for k, v in cache.items():
            if v == n:
                ans = min(ans, k)

        return ans if ans != float('inf') else -1
    
print(Solution().smallestCommonElement([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]])) # 5