# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/

import math


class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        def check(k):
            cur = 0

            for num in nums:
                cur += math.ceil(num / k)

            return cur <= threshold

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


print(Solution().smallestDivisor(nums=[1, 2, 5, 9], threshold=6))  # 5
