from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        cache = defaultdict(list)
        ans = 0
        total = 0
        cache[0].append(-1)

        for i, num in enumerate(nums):
            total += 1 * (1 if num else -1)

            if total in cache:
                ans = max(ans, i - cache[total][0])

            cache[total].append(i)

        return ans

print(Solution().findMaxLength([0,1,0])) # 2