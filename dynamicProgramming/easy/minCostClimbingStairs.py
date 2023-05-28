# https://leetcode.com/problems/min-cost-climbing-stairs/

from functools import cache


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        @cache
        def dp(i: int) -> int:
            if i <= 1:
                return 1
            return min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])

        return dp(len(cost))


print(Solution().minCostClimbingStairs(cost=[10, 15, 20]))  # 15
print(Solution().minCostClimbingStairs(
    cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
