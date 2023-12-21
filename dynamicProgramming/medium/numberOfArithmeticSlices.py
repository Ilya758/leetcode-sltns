class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1

        print(dp)

        return sum(dp)

print(Solution().numberOfArithmeticSlices([1, 2, 3, 4])) # 3