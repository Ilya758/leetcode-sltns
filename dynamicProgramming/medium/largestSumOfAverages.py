from functools import cache

class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        p = [0]
        n = len(nums)

        for i in range(n):
            p.append(p[-1] + nums[i])

        @cache
        def dp(i, remain):
            if remain == 1:
                return (p[n] - p[i]) / (n - i)

            return max((p[j] - p[i]) / (j - i) + dp(j, remain - 1) for j in range(i + 1, n - remain + 2))
            
        return dp(0, k)

print(Solution().largestSumOfAverages([1, 2], k = 2)) # 3
