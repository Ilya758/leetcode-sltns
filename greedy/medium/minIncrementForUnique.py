class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        prev = nums[0]
        ans = 0

        for i in range(1, len(nums)):
            if prev >= nums[i]:
                ans += prev - nums[i] + 1
                prev += 1
            else:
                prev = nums[i]

        return ans

print(Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7])) # 6