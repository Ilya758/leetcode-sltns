from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        cache = defaultdict(list)
        ans = 0

        for w in words:
            cache[w[0]].append(w[1:])

        for ch in s:
            prev = cache[ch]
            cache[ch] = []

            for suf in prev:
                if suf:
                    cache[suf[0]].append(suf[1:])
                else:
                    ans += 1

        return ans

print(Solution().numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"])) # 3
