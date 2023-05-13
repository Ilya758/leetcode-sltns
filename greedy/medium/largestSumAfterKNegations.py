# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

from heapq import *


class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        heapify(nums)

        while k:
            num = -heappop(nums)
            k -= 1
            heappush(nums, num)

        return sum(nums)


print(Solution().largestSumAfterKNegations(nums=[4, 2, 3], k=1))  # 5
