# https://leetcode.com/problems/koko-eating-bananas/description/

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def check(k):
            cur = 0

            for pile in piles:
                cur += math.ceil(pile / k)

            return cur <= h

        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                # if it can eat all of the bananas for h
                right = mid - 1
            else:
                # otherwise, we'll need to increase the speed
                left = mid + 1

        return left


print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8))  # 4
