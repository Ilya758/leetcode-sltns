from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(remain, s):
            if not remain:
                return int(s == target)

            if s > target:
                return 0

            res = 0

            for i in range(1, k + 1):
                res = (res + dp(remain - 1, s + i)) % MOD

            return res

        return dp(n, 0)


print(Solution().numRollsToTarget(2, 6, 7)) # 6