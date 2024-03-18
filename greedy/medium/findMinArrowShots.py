class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = lambda x: x[1])
        ans = 0
        end = float("-inf")
        
        for a, b in points:
            if end < a:
                end = b
                ans += 1

        return ans

print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])) # 2
