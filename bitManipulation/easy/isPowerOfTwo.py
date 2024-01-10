class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1

        while True:
            if x == n:
                return True
            elif x > n:
                return False
            
            x <<= 1

print(Solution().isPowerOfTwo(8)) # True