class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        def isVowel(char):
            return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' 

        def getScore(word):
            return int(isVowel(word[0]) and isVowel(word[-1]))

        prefix = [0]
        n = len(words)
        ans = []

        for i in range(n):
            prefix.append(prefix[-1] + getScore(words[i]))

        for a, b in queries:
            ans.append(prefix[b + 1] - prefix[a])

        return ans
    
print(Solution().vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]])) # [2,3,0] 