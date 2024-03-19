class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        n, m = len(s), len(spaces)
        j = 0
        ans = []

        for i in range(n):
            if j != m:
                if i == spaces[j]:
                    ans.append(' ')
                    j += 1

            ans.append(s[i])

        return "".join(ans)
    
print(Solution().addSpaces(s = "icodeinpython", spaces = [1,5,7,9])) 
# "i code in py thon"