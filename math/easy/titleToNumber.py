class Solution:
    def titleToNumber(self, s: str) -> int:
        c = len(s) - 1
        ans = 0

        for char in s:
            order = ord(char.lower()) - 97 + 1
            ans += order * (26 ** c)
            c -= 1

        return ans

print(Solution().titleToNumber('ZY'))