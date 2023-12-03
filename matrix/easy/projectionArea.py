class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        yx = sum([sum([1 if col else 0 for col in row]) for row in grid])
        xy = sum([max(row) for row in grid])
        zy = sum([max([grid[col][row] for col in range(len(grid[0]))]) for row in range(len(grid))]) 

        return yx + xy + zy

print(Solution().projectionArea(grid = [[1,2],[3,4]]))