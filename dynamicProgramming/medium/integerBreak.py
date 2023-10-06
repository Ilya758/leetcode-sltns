from functools import cache


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1

        @cache
        def dp(k):
            if k <= 3:
                return k
            
            result = 1

            for i in range(2, k):
                result = max(result, i * dp(k - i))

            return result

        return dp(n)
    
print(Solution().integerBreak(10)) # 36