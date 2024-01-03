class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        ones = nums.count(1)
        nums += nums
        cur = nums[:ones].count(0)
        ans = cur
        n = len(nums)

        for i in range(ones, n):
            cur += int(nums[i] == 0) - int(nums[i-ones] == 0)
            ans = min(ans, cur)
        
        return ans
        
print(Solution().minSwaps(nums = [0,1,0,1,1,0,0])) # 1