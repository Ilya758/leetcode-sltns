from functools import cache


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n = len(dictionary)
        dictSet = set(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0

            ans = 1 + dp(start + 1)

            for end in range(start, n):
                sub = s[start:end + 1]

                if sub in dictSet:
                    ans = min(ans, dp(end + 1))

            return ans

        return dp(0)

print( Solution().minExtraChar(s='dwmodizxvvbosxxw', dictionary=["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"])) # 7
