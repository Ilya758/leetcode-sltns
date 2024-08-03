from heapq import *


class Solution:
    def makePrefSumNonNegative(self, nums: list[int]) -> int:
        ans = prefix = 0
        heap = []

        for num in nums:
            prefix += num

            if num < 0:
                heappush(heap, num)

            if prefix < 0:
                prefix -= heappop(heap)
                ans += 1

        return ans

print(Solution().makePrefSumNonNegative([-5,-3,3,-4,0,3,0,-3,4,5])) # 3