class Solution:
    def minAvailableDuration(self, A: list[list[int]], B: list[list[int]], dur: int) -> list[int]:
        i = j = 0
        A.sort()
        B.sort()

        while i < len(A) and j < len(B):
            a, b = A[i]
            c, d = B[j]
            minStart = max(a, c)
            minEnd = min(b, d)

            if minStart + dur <= minEnd:
                return [minStart, minStart + dur]
            
            if b < d:
                i += 1
            else:
                j += 1
            
        return []

print(Solution().minAvailableDuration(A = [[10,12],[15, 25]], B =[[0,100]], dur = 8)) # [15, 23]