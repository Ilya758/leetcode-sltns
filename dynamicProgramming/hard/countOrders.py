from functools import cache


class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dp(i, j):
            if i == j == n:
                return 1
            
            if j > i or i > n or j > n:
                return 0

            ways = ((i - j) * dp(i, j + 1)) % mod
            ways += ((n - i) * dp(i + 1, j)) % mod

            return ways

        return dp(0, 0)
    
print(Solution().countOrders(n = 3)) # 90


