class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        level = [poured]

        for i in range(query_row):
            nextLevel = [0.0] * (i + 2)

            for glass in range(len(level)):
                overflow = (level[glass] - 1) / 2

                if overflow > 0.0:
                    nextLevel[glass] += overflow
                    nextLevel[glass + 1] += overflow

            level = nextLevel
        
        return min(1.0, level[query_glass])
    
print(Solution().champagneTower(poured = 100000009, query_row = 33, query_glass = 17
)) # 1.0