class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        left = 0
        ans = 0
        x = 0
        nums.sort(reverse=True)
        
        for right in range(len(nums)):
            x += nums[left] - nums[right]

            while x > k:
                diff = nums[left] - nums[left + 1]
                x -= diff * (right - left)
                left += 1

            ans = max(ans, right - left + 1)
            
        return ans

print(Solution().maxFrequency(nums = [1,2,4], k = 5)) # 3