class Solution:
    def countBits(self, n: int) -> list[int]:
        return [bin(x).count('1') for x in range(0, n + 1)]
    
print(Solution().countBits(5)) # [0,1,1,2,1,2]