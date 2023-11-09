from math import floor


class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        left = 0
        right = 1

        def count(n):
            return n * (n + 1) / 2

        while right < len(s):
            if s[right - 1] != s[right]:
                ans += count(right - left)
                left = right

            right += 1
             
        return floor((ans + count(right - left)) % (1e9 + 7))
    
print(Solution().countHomogenous(s='abbcccaa')) # 13