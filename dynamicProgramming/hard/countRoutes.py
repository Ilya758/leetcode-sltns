# https://leetcode.com/problems/count-all-possible-routes/description/

from functools import cache
import math


class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        mod = 1e9 + 7
        n = len(locations)

        def getDiff(a, b):
            return abs(locations[a] - locations[b])

        # 1. state include index of a city and amount of fuel

        @cache
        def dp(i, remain):
            cur = 0

            # 2. any time we have a fuel
            if remain >= 0:
                # 2.1 and reach the city, add it to the answer
                if i == finish:
                    cur += 1
            # 3. otherwise it's impossible to reach the city
            # since we're out of fuel
            else:
                return 0

            # 4. iterate over indices of cities to find
            # if we can reach the other city
            for j in range(n):
                if j != i:
                    # 4.1 the recurrence relation is static
                    cur += dp(j, remain - getDiff(i, j))

            # since the answer can be large, return it modulo
            return cur % mod

        return math.floor(dp(start, fuel))


print(Solution().countRoutes(
    locations=[2, 3, 6, 8, 4], start=1, finish=3, fuel=5))  # 4
print(Solution().countRoutes(
    locations=[4, 3, 1], start=1, finish=0, fuel=6
))  # 5
print(Solution().countRoutes(
    locations=[5, 2, 1], start=0, finish=2, fuel=3
))  # 0
