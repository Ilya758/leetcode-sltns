class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        left = min(nums) + k
        right = max(max(nums) - k, left)

        return right - left

print(Solution().smallestRangeI(nums = [1,3,6], k = 3)) # 0