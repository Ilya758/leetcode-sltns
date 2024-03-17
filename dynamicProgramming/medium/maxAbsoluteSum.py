class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][0] = min(dp[i - 1][0] + nums[i], nums[i])
            dp[i][1] = max(dp[i - 1][1] + nums[i], nums[i])
            ans = max(ans, abs(dp[i][0]), dp[i][1])

        return ans

print(Solution().maxAbsoluteSum([2, -5, 1, 2, 3, 4, 5])) # 15