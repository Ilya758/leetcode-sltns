# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/
from collections import Counter


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        map = Counter(nums)
        curMax = max(map.values())
        ans = [[] for _ in range(curMax)]

        for k, v in map.items():
            for i in range(v):
                ans[i].append(k)

        return ans


print(Solution().findMatrix(nums=[1, 3, 4, 1, 2, 3, 1]))
# [[1,3,4,2],[1,3],[1]]
