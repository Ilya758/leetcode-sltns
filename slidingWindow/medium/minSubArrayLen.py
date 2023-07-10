# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        prefix = 0
        left = 0
        right = 0
        ans = float('inf')
        n = len(nums)

        for right in range(n):
            prefix += nums[right]

            while prefix >= target:
                ans = min(ans, right - left + 1)
                prefix -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans


print(Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))  # 2
print(Solution().minSubArrayLen(target=4, nums=[1, 4, 4]))  # 1
print(Solution().minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))  # 0
