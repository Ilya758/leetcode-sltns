from functools import cache


class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def dp(s, k):
            if k == n: return 1

            return sum([dp(x, k + 1) for x in ['a','e','i','o','u'] if s <= x])

        return dp('a', 0)
    
print(Solution().countVowelStrings(n = 33)) # 66045