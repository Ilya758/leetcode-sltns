# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        chars = defaultdict(int)
        cur = 0
        ans = 0

        for right in range(len(s)):
            cur += 1
            chars[s[right]] += 1

            while chars[s[right]] > 1:
                cur -= 1
                chars[s[left]] -= 1
                left += 1

            ans = max(ans, cur)

        return ans


print(Solution().lengthOfLongestSubstring(s="abcabcbb"))  # 3
