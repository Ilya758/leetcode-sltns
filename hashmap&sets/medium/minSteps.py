from collections import defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cache = defaultdict(int)

        for char in s:
            cache[char] += 1

        for char in t:
            cache[char] -= 1

        return sum([abs(x) for x in cache.values()])
    
print(Solution().minSteps("anagram", "nagaram")) # 0