class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        cache = dict()
        ans = 0

        for word in words:
            if word in cache: ans += 1
            else: cache[''.join(reversed(word))] = True

        return ans
    
print(Solution().maximumNumberOfStringPairs(words = ["cd","ac","dc","ca","zz"])) # 2 