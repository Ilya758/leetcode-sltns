class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                diff = abs(nums[i] - nums[i - 1]) + 1
                nums[i] += diff
                ans += diff

        return ans
    
print(Solution().minOperations(nums = [1,5,2,4,1])) # 14