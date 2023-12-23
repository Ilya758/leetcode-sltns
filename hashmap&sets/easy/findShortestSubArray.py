from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        cache = defaultdict(list)
        curMax = 0

        for i in range(len(nums)):
            cache[nums[i]].append(i)
            
            if len(cache[nums[i]]) > curMax:
                curMax = len(cache[nums[i]])

        ans = float('inf')

        for v in cache.values():
            if len(v) == curMax:
                ans = min(ans, v[-1] - v[0] + 1)

        return ans

print(Solution().findShortestSubArray([1,2,2,3,1])) # 2