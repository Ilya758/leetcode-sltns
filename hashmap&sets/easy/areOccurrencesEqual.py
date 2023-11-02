from collections import defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cache = defaultdict(int)

        for char in s:
            cache[char] += 1

        return len(set(cache.values())) == 1
    
print(Solution().areOccurrencesEqual("aaabbb")) # True