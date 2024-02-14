class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        left = 0
        ans = 2 if nums[0] + 1 == nums[1] else -1
        pos = True

        for right in range(1, len(nums)):
            prev, cur = nums[right - 1], nums[right]

            if prev + (1 if pos else -1) != cur:
                left = right - 1 if nums[right - 1] + 1 == nums[right] else right
                pos = bool(left == right)
            else:
                ans = max(ans, right - left + 1)
                pos = not pos

        return ans

print(Solution().alternatingSubarray(nums = [2,3,4,3,4])) # 4
