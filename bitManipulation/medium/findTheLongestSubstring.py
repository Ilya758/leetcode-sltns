class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        XOR = 0
        cache = {XOR: -1}
        ans = 0

        for i, ch in enumerate(s):
            if (ch in vowels): XOR ^= vowels[ch]

            if XOR not in cache:
                cache[XOR] = i
            else:
                ans = max(ans, i - cache[XOR])

        return ans
    
print(Solution().findTheLongestSubstring(s = "eleetminicoworoep")) # 13 