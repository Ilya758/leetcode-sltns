# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

import math


class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        if len(dist) > math.ceil(hour):
            return -1

        def check(k):
            h = 0

            for d in dist:
                h = math.ceil(h) + d / k

            return h <= hour

        left = 1
        right = 10 ** 7

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


print(Solution().minSpeedOnTime(dist=[1, 3, 2], hour=6))  # 1
