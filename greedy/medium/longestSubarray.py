class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        ans = 1
        AND = maxSoFar = nums[0]
        left = 0

        for right in range(1, len(nums)):
            AND &= nums[right]

            if nums[right] > maxSoFar:
                ans = 1
                maxSoFar = AND = nums[right]
                left = right
            elif AND == maxSoFar:
                ans = max(ans, right - left + 1)
            else:
                left = right
                AND = nums[right]

        return ans

print(Solution().longestSubarray([1,2,3,3,2,2])) # 2

