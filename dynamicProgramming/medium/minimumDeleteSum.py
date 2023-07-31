# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/

from functools import cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)

        # at each step we need to know
        @cache
        def dp(i, j):
            # if we're out of free chars
            if i == n and j == m:
                return 0

            # any time there're some chars in s1
            if i < n:
                # and s2
                if j < m:
                    # and both equals
                    if s1[i] == s2[j]:
                        return dp(i + 1, j + 1)

                    # otherwise find a minimum ascii diff
                    return min(ord(s1[i]) + dp(i + 1, j), ord(s2[j]) + dp(i, j + 1))

                # we're out of chars in s2
                return ord(s1[i]) + dp(i + 1, j)
            else:
                # we're out of chars in s1
                return ord(s2[j]) + dp(i, j + 1)

        return dp(0, 0)


print(Solution().minimumDeleteSum(s1="sea", s2="eat"))  # 231
print(Solution().minimumDeleteSum(s1="delete", s2="leet"))  # 403
