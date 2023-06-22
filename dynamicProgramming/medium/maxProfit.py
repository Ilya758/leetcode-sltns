# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

from functools import cache


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        # the recurrence relation is dynamic and include 3 possible transitions
        @cache
        def dp(i, holding):
            if i == len(prices):
                return 0

            # 1. either we're holding a stock and do nothing
            ans = dp(i + 1, holding)

            # 2. once we had a stock, we can sell it
            if holding:
                ans = max(ans, prices[i] - fee + dp(i + 1, False))
            # 3. if not, just buy it
            else:
                ans = max(ans, -prices[i] + dp(i + 1, True))

            return ans

        return dp(0, False)


print(Solution().maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))  # 8
