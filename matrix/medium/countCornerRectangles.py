from typing import Counter


class Solution(object):
    def countCornerRectangles(self, grid):
        count = Counter()
        ans = 0

        for row in grid:
            for c1, v1 in enumerate(row):
                if v1:
                    for c2 in range(c1+1, len(row)):
                        if row[c2]:
                            ans += count[c1, c2]
                            count[c1, c2] += 1
                            
        return ans
    
print(Solution().countCornerRectangles(grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1],[0,1,0,1,0]])) # 1