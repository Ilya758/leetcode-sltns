class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = [''] * n
        left = 0

        for right in range(n - 1, (n - 1) // 2 - 1, -1):
            if s[left] <= s[right]:
                [ans[left], ans[right]] = [s[left], s[left]]
            else: 
                [ans[left], ans[right]] = [s[right], s[right]] 
            
            left += 1

        return "".join(ans)
    
print(Solution().makeSmallestPalindrome(s = "egcfe")) # "efcfe"