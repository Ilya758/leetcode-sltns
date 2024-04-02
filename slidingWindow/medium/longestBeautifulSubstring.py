class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        cache = {word[0]}
        ans = i = 0

        for j in range(1, len(word)):
            if word[j] < word[j - 1]:
                cache.clear()
                i = j

            cache.add(word[j])

            if len(cache) == 5:
                ans = max(ans, j - i + 1)

        return ans
    
print(Solution().longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu")) # 13