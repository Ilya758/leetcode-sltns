# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/
from collections import defaultdict
from functools import reduce


class Solution:
    def countBalls(self, l: int, h: int) -> int:
        cache = defaultdict(int)
        ans = 0

        for i in range(l, h + 1):
            key = reduce(lambda a, c: a + c, map(int, list(str(i))))
            cache[key] += 1
            ans = max(ans, cache[key])

        return ans


print(Solution().countBalls(l=1, h=10))
