from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCache = defaultdict(int)
        
        for char in t:
            tCache[char] += 1

        left = 0
        count = float('inf')
        idx = 0
        cache = defaultdict(int)
        cur = len(tCache)

        for right in range(len(s)):
            if s[right] in tCache:
                cache[s[right]] += 1

                if cache[s[right]] == tCache[s[right]]:
                    cur -= 1

            while cur == 0:
                if count > right - left + 1:
                    count = right - left + 1
                    idx = left

                if s[left] in tCache:
                    cache[s[left]] -= 1

                    if cache[s[left]] < tCache[s[left]]:
                        cur += 1

                left += 1

        return s[idx:idx + count] if count != float('inf') else ''
