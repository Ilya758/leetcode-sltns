class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        k = sum(nums)

        if k & 1:
            return False
            
        k //= 2
        n = len(nums)
        dp = [[False] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            curr = nums[i - 1]

            for j in range(k + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]

        return dp[n][k]

print(Solution().canPartition([3,3,3,4,5])) # True