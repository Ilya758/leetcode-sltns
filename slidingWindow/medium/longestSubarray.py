# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zerosCount = 0
        ans = 0

        for right in range(len(nums)):
            zerosCount += int(nums[right] == 0)

            while zerosCount > 1:
                zerosCount -= int(nums[left] == 0)
                left += 1

            ans = max(ans, right - left)

        return ans


print(Solution().longestSubarray(nums=[1, 1, 0, 1]))  # 3
print(Solution().longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))  # 5
print(Solution().longestSubarray(nums=[1, 1, 1]))  # 2
