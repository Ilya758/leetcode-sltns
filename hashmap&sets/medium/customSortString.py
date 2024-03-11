from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cache = defaultdict(int)
        freqs = [0] * 26
        suffix = ""

        for i, char in enumerate(order):
            cache[char] = i
            cache[i] = char

        for char in s:
            if char in cache:
                freqs[cache[char]] += 1
            else:
                suffix += char

        return ''.join(cache[i] * c for i, c in enumerate(freqs) if c) + suffix

print(Solution().customSortString(order = "cba", s = "abcd")) # cbad