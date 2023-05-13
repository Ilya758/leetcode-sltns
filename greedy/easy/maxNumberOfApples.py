# https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/description/

from heapq import *


class Solution:
    def maxNumberOfApples(self, weight: list[int]) -> int:
        heapify(weight)
        n = len(weight)
        total = 0
        ans = 0

        while ans < n:
            item = heappop(weight)

            if total + item <= 5000:
                total += item
                ans += 1
            else:
                break

        return ans


print(Solution().maxNumberOfApples(weight=[100, 200, 150, 1000]))  # 4
