from collections import defaultdict


class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        rects = defaultdict(int)

        for a, b in rectangles:
            rects[min(a, b)] += 1

        ans = 0
        maxFreq = 0

        for k, v in rects.items():
            if k > maxFreq:
                maxFreq = k
                ans = v

        return ans
    
print(Solution().countGoodRectangles(rectangles = [[5,8],[3,9],[5,12],[16,5]])) # 3