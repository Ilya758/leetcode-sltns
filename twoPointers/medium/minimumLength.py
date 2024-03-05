class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                break
            
            target = s[left]
            
            while left <= right and s[left] == target:
                left += 1
            while left <= right and s[right] == target:
                right -= 1

        return right - left + 1

print(Solution().minimumLength("abbbbbbbbbbbbbbbbbbba")) # 0