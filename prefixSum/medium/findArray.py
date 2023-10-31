class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        ans = [pref[0]]

        for i in range(1, len(pref)): ans.append(pref[i] ^ pref[i - 1])

        return ans
    
print(Solution().findArray(pref = [5,2,0,3,1])) # [5,7,2,3,2]