# https://leetcode.com/problems/house-robber/

from functools import cache


class Solution:
    def rob(self, nums: list[int]) -> int:
        @cache
        def dp(i: int) -> int:
            if i <= 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(dp(i - 1), dp(i - 2) + nums[i])

        return dp(len(nums) - 1)


print(Solution().rob(nums=[2, 7, 9, 3, 1]))  # 12
