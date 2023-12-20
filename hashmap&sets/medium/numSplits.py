from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        ans = 0
        cache = Counter(s)
        left = set()
        right = set(s)

        for token in s:
            cache[token] -= 1
            left.add(token)
            
            if cache[token] == 0:
                right.remove(token)

            if len(left) == len(right):
                ans += 1

        return ans

print(Solution().numSplits("aacaba")) # 2