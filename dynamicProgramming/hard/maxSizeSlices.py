class Solution:
    def maxSizeSlices(self, slices: list[int]) -> int:
        n = len(slices)
        m = n // 3

        def get(nums):
            k = len(nums)
            dp = [[0] * (m + 1) for _ in range(k + 1)]

            for i in range(1, k + 1):
                for j in range(1, m + 1):
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i - 2][j - 1] + nums[i - 1]
                    )

            return dp[k][m]

        return max(get(slices[1:]), get(slices[:-1]))
    
print(Solution().maxSizeSlices([1,2,3,4,5,6])) # 10