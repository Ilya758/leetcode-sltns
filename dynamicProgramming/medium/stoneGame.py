from functools import cache


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        @cache
        def dp(i, j):
            if i > j:
                return 0
            
            left, right = piles[i] - piles[j], piles[j] - piles[i]
            
            return max(dp(i + 1, j - 1) + left, dp(i + 1, j - 1) + right)

        return dp(0, len(piles) - 1)
    
print(Solution().stoneGame([5,3,4,5])) # True