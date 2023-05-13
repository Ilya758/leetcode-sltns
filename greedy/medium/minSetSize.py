# https://leetcode.com/problems/reduce-array-size-to-the-half/description/

from collections import Counter
import math


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        map = Counter(arr)
        vals = sorted(map.values(), reverse=True)
        total = 0
        ans = 0
        n = math.ceil(len(arr) / 2)

        for num in vals:
            total += num
            ans += 1

            if total >= n:
                break

        return ans


print(Solution().minSetSize(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))  # 2
