class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0

        for cur in range(1, len(set(s)) + 1):
            left = right = unique = atLeastK = 0
            freqs = [0] * 26

            while right < len(s):
                if unique <= cur:
                    idx = ord(s[right]) - 97

                    if freqs[idx] == 0:
                        unique += 1
                    freqs[idx] += 1

                    if freqs[idx] == k:
                        atLeastK += 1
                    right += 1
                else:
                    idx = ord(s[left]) - 97

                    if freqs[idx] == k:
                        atLeastK -= 1
                    freqs[idx] -= 1
                    
                    if freqs[idx] == 0:
                        unique -= 1
                    left += 1

                if unique == atLeastK:
                    ans = max(ans, right - left)

        return ans


print(Solution().longestSubstring(s = "ababbc", k = 2)) # 5