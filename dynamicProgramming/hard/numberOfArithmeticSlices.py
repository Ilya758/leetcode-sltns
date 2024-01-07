from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        dp = [defaultdict(int) for _ in nums]
        ans = 0

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1

                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    ans += dp[j][diff]

        return ans

print(Solution().numberOfArithmeticSlices([7,7,7,7,7])) # 16