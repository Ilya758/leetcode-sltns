class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        order = {t: i for i, t in enumerate(keyboard)}
        ans = order[word[0]]

        for i in range(1, len(word)):
            ans += abs(order[word[i - 1]] - order[word[i]])

        return ans
    
print(Solution().calculateTime(keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba")) # 4