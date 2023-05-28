from functools import cache


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 0
            if i < 0:
                return float('inf')
            return min([dp(i - c) + 1 for c in coins])

        ans = dp(amount)

        return -1 if ans == float('inf') else ans


print(Solution().coinChange(coins=[1, 2, 5], amount=11))  # 3
