class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            curMax = arr[i]

            for j in range(i, max(-1, i - k), -1):
                curMax = max(curMax, arr[j])
                dp[j] = max(dp[j], (i - j + 1) * curMax + dp[i + 1])

        return dp[0]

print(Solution().maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3))