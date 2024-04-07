from functools import cache


class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dp(i, k):
            if i == len(s):
                return not k
            if k < 0:
                return False

            res = False

            if s[i] == '*':
                res = dp(i + 1, k) or dp(i + 1, k - 1) or dp(i + 1, k + 1)
            else:
                res = dp(i + 1, k + (1 if s[i] == '(' else -1))

            return res

        return dp(0, 0)

print(Solution().checkValidString('()')) # True