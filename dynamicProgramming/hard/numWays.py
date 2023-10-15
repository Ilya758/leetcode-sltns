from functools import cache
import math


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def dp(i, remain):
            if not remain:
                return 1 if not i else 0

            remain -= 1
            result = dp(i, remain)

            if i > 0: result += dp(i - 1, remain)
            if i < arrLen - 1: result += dp(i + 1, remain)

            return math.floor(result % (1e9 + 7))

        return dp(0, steps)

print(Solution().numWays(3, 2)) # 4