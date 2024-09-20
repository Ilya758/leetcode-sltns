class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)

        if not n:
            return ""

        left = 0

        for right in range(n - 1, -1, -1):
            if s[right] == s[left]:
                left += 1

        if left == n:
            return s

        suffix = s[left:]
        prefix = suffix[::-1]

        return prefix + self.shortestPalindrome(s[:left]) + suffix
        
print(Solution().shortestPalindrome('abc')) # cbabc