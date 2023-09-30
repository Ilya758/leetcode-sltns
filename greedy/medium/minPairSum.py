class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = float('-inf')

        while left < right:
            ans = max(ans, nums[left] + nums[right])
            left += 1
            right -= 1

        return ans
    
print(Solution().minPairSum(nums = [3,5,2,3])) # 7