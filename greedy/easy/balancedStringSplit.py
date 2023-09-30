class Solution:
    def balancedStringSplit(self, s: str) -> int:
        chars = {'L': -1, 'R': 1}
        ans, cur = 0, 0

        for right in range(len(s)):
            cur += chars[s[right]]

            if cur == 0: ans += 1

        return ans
    
print(Solution().balancedStringSplit(s = "RLRRLLRLRL")) # 4