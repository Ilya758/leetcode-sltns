class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freqs = [0] * 26

        for i in range(len(t)):
            freqs[ord(t[i]) - 97] += 1

            if i < len(s):
                freqs[ord(s[i]) - 97] -= 1

        return chr([i for i, v in enumerate(freqs) if v == 1][0] + 97)

print(Solution().findTheDifference("a", 'aa'))