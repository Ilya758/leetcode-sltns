from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        cache = defaultdict(int)

        for a, b in dominoes:
            pair = [b, a] if a > b else [a, b]
            cache[tuple(pair)] += 1

        return sum([v * (v - 1) // 2 for v in cache.values() if v > 1])
    
print(Solution().numEquivDominoPairs(dominoes = [[1,2],[2,1],[3,4],[5,6]])) # 1