from functools import cache


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        @cache
        def dp(i: int) -> int:
            ans = 1

            for j in range(i):
                if nums[i] > nums[j]:
                    ans = max(ans, dp(j) + 1)

            return ans

        return max([dp(i) for i in range(len(nums))])


print(Solution().lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))  # 4
