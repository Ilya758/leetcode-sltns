class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        ans = 0

        while diff:
            if diff & 1:
                ans += 1
            diff >>= 1

        return ans
        
print(Solution().hammingDistance(1,4)) # 2