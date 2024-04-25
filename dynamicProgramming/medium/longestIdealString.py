class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        ans = 0

        for i in range(len(s)):
            cur = ord(s[i]) - 97
            maxCount = 0

            for prev in range(26):
                if abs(prev - cur) <= k:
                    maxCount = max(maxCount, dp[prev])

            dp[cur] = max(dp[cur], maxCount + 1)
            ans = max(ans, dp[cur])

        return ans
    
print(Solution().longestIdealString(s = "abcd", k = 3)) # 4