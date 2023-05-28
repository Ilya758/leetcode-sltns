from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(step: int) -> int:
            if step <= 1:
                return 1

            return dp(step - 1) + dp(step - 2)

        return dp(n)


print(Solution().climbStairs(4))  # 5
