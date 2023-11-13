class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        pattern = set({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})
        ans = []

        for i, char in enumerate(s):
            if char.lower() in pattern: vowels.append(char)

        vowels.sort()
        j = 0   

        print(vowels, s)

        for char in s:
            if char in pattern:
                ans.append(vowels[j])
                j += 1
            else: ans.append(char)

        return ''.join(ans)
    
print(Solution().sortVowels('lEetcOde'))