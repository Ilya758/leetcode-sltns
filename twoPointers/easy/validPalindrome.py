class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(i: int, j: int) -> bool:
            return all(s[k] == s[j - k + i] for k in range(i, j))

        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                
                return check(i + 1, j) or check(i, j - 1)
                
        return True

print(Solution().validPalindrome("acbba")) # True