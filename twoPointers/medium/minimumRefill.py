class Solution:
    def minimumRefill(self, plants: list[int], A: int, B: int) -> int:
        ans = 0
        i, j = 0, len(plants) - 1
        volA, volB = A, B

        while i < j:
            a, b = plants[i], plants[j]
            aV = a <= volA 
            bV = b <= volB
            ans += int(not aV) + int(not bV)
            volA = (volA if aV else A) - a 
            volB = (volB if bV else B) - b 
            i += 1
            j -= 1

        if i == j:
            ans += int(max(volA, volB) < plants[i])

        return ans
    
print(Solution().minimumRefill([5], 10, 8)) # 1