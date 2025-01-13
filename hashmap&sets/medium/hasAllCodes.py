from collections import defaultdict


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        cache = defaultdict(int)
        base = 29
        hash = 0
        mod = 10 ** 9 + 7
        basePow = pow(base, k - 1, mod)
        n = len(s)

        for i in range(min(n, k)):
            hash = (hash * base + ord(s[i])) % mod

        cache[hash] += 1

        for i in range(k, n):
            hash = (hash - ord(s[i-k]) * basePow) % mod
            hash = (hash * base + ord(s[i])) % mod
            cache[hash] += 1

        return len(cache) == 2 ** k
    
print(Solution().hasAllCodes(s = "00110110", k = 2)) # True