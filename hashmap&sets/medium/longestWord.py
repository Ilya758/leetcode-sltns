class Solution:
    def longestWord(self, words: list[str]) -> str:
        seen = set()
        ans = ''

        for w in sorted(words): 
            if len(w) == 1 or w[:-1] in seen:
                seen.add(w)

                if len(w) > len(ans):
                    ans = w

        return ans
    
print(Solution().longestWord(["w","wo","wor","worl","world"])) # world