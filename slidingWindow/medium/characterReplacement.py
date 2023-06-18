from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        map = defaultdict(int)
        n = len(s)

        for right in range(n):
            map[s[right]] += 1

            while right - left + 1 - max(map.values()) > k:
                map[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


print(Solution().characterReplacement(s="ABCDE", k=1))  # 2
print(Solution().characterReplacement(s="ABAB", k=2))  # 4
