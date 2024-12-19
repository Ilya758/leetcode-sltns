from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def get(x):
            cache = defaultdict(int)
            res = left = 0
            cons = 0

            for right, ch in enumerate(word):
                if ch in 'aeiou':
                    cache[ch] += 1
                else:
                    cons += 1

                while len(cache) == 5 and cons > x:
                    print(word[left:right+1])
                    if word[left] in 'aeiou':
                        cache[word[left]] -= 1

                        if not cache[word[left]]:
                            del cache[word[left]]
                    else:
                        cons -= 1

                    left += 1

                res += right - left + 1

            return res

        return get(k) - get(k - 1)
    
print(Solution().countOfSubstrings(word = "abeiou", k = 1)) # 1