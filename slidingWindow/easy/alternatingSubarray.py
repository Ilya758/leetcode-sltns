class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        left = 0
        ans = 2 if nums[0] + 1 == nums[1] else -1
        sign = 1

        for right in range(1, len(nums)):
            prev, cur = nums[right - 1], nums[right]

            if prev + sign != cur:
                left = right - int(prev + 1 == nums[right])
                sign = 1 if left == right else -1
            else:
                ans = max(ans, right - left + 1)
                sign *= -1

        return ans


print(Solution().alternatingSubarray(nums = [2,3,4,3,4])) # 4
