# https://leetcode.com/problems/coin-change-ii/description/
from functools import cache


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # NOT OPTIMAL SOLUTION
        n = len(coins)

        @cache
        def dp(i, j):
            if i == 0:
                return 1
            if i < 0 or j == n:
                return 0
            return sum([dp(i - coins[k], k) for k in range(j, n)])

        return dp(amount, 0)


print(Solution().change(amount=5, coins=[1, 2, 5]))  # 4
