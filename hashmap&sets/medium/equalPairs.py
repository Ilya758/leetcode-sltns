from collections import defaultdict


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rowMap = defaultdict(int)
        colMap = defaultdict(int)

        def keify(nums):
            return ",".join([str(num) for num in nums])

        for nums in grid:
            pair = keify(nums)
            rowMap[pair] = rowMap[pair] + 1

        for i in range(len(grid)):
            col = []

            for j in range(len(grid[0])):
                col.append(grid[j][i])

            pair = keify(col)
            colMap[pair] = colMap[pair] + 1

        ans = 0

        for k, v in rowMap.items():
            if k in colMap:
                ans += v * colMap[k]

        return ans


print(Solution().equalPairs(
    grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))  # 3
