class Solution:
    def removeInterval(self, intervals: list[list[int]], toBeRemoved: list[int]) -> list[list[int]]:
        ans = []
        a, b = toBeRemoved

        for start, end in intervals:
            if start < a < end:
                ans.append([start, a])
            if start < b < end:
                ans.append([b, end])
            if b < start or a > end:
                ans.append([start, end])

        return ans
    
print(Solution().removeInterval(intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4])) # [[-5, -4], [-3, -2], [4, 5], [8, 9]]