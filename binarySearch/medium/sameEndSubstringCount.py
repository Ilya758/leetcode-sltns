from bisect import *
from collections import defaultdict


class Solution:
    def sameEndSubstringCount(self, s: str, queries: list[list[int]]) -> list[int]:
        cache = defaultdict(list)
        ans = []

        for i, t in enumerate(s):
            cache[t].append(i)

        for a, b in queries:
            res = 0

            for values in cache.values():
                left = bisect_left(values, a)
                right = bisect_right(values, b)
                diff = right - left
                res += diff * (diff + 1) // 2

            ans.append(res)

        return ans

print(Solution().sameEndSubstringCount(s = "abcaab", queries = [[0,0],[1,4],[2,5],[0,5]]))