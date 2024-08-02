from heapq import *


class Solution:
    def findScore(self, nums: list[int]) -> int:
        seen = set()
        heap = []
        n = len(nums)
        ans = 0

        for i in range(n):
            heappush(heap, (nums[i], i))

        while len(seen) != n:
            score, i = heappop(heap)
            
            if i not in seen:
                ans += score
                seen.add(i)

                if i > 0:
                    seen.add(i - 1)
                if i < n - 1:
                    seen.add(i + 1)

        return ans
    
print(Solution().findScore([1,2,3,4,5,6,7])) # 16