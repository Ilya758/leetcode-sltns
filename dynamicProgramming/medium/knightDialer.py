from functools import cache


class Solution:
    def knightDialer(self, n: int) -> int:
        ans = 0
        mod = 10 ** 9 + 7
    
        @cache
        def dp(remain, square):
            if remain == 0:
                return 1
            
            ans = 0

            for nextSquare in jumps[square]:
                ans = (ans + dp(remain - 1, nextSquare)) % mod
            
            return ans
        
        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        for square in range(10):
            ans = (ans + dp(n - 1, square)) % mod
        
        return ans

print(Solution().knightDialer(2)) # 20