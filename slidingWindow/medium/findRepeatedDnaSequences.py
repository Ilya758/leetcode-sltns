from collections import defaultdict, deque


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        q = deque([char for char in s[:9]])
        cache = defaultdict(int)

        for i in range(9, len(s)):
            q.append(s[i])
            cache[''.join(q)] += 1
            q.popleft()

        return [k for k, v in cache.items() if v > 1]

print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) # ["AAAAACCCCC", "CCCCCAAAAA"]