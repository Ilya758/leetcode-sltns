from heapq import *
from math import gcd


class Solution:
    def minOperations(self, nums: list[int], x: list[int]) -> int:
        commonGcd = x[0]

        for i in range(1, len(x)):
            commonGcd = min(commonGcd, gcd(x[i], commonGcd))

        heapify(nums)
        ans = 0

        while nums:
            num = heappop(nums)

            if commonGcd >= num and commonGcd % num == 0:
                return ans

            ans += 1

        return -1
    
print(Solution().minOperations(nums = [2,3,2,4,3], x = [9,6,9,3,15])) # 2