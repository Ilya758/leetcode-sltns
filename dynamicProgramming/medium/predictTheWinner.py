# https://leetcode.com/problems/predict-the-winner/description/
from functools import cache


class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        @cache
        def dp(start, end):
            if start == end:
                return nums[start]

            left = nums[start] - dp(start + 1, end)
            right = nums[end] - dp(start, end - 1)

            return max(left, right)

        return dp(0, len(nums) - 1) >= 0


print(Solution().PredictTheWinner(nums=[1, 5, 2]))  # False
print(Solution().PredictTheWinner(nums=[1, 5, 233, 7]))  # True
