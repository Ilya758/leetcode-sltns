from functools import cache


class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        @cache
        def dp(i, remain):
            if remain <= 0:
                return 0
            if i == n:
                return float('inf')
            
            paint = cost[i] + dp(i + 1, remain - 1 - time[i])
            dont_paint = dp(i + 1, remain)

            return min(paint, dont_paint)
    
        n = len(cost)

        return dp(0, n)
    
print(Solution().paintWalls(cost = [1,2,3,2], time = [1,2,3,2]
)) # 3