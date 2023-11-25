class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        prefix = [nums[0]]
        n = len(nums)

        for i in range(1, n): prefix.append(prefix[i - 1] + nums[i])

        ans = []
        
        for i in range(len(nums)):
            left = nums[i] * (i + 1) - prefix[i]
            right = prefix[-1] - prefix[i] - nums[i] * (n - i - 1)
            ans.append(left + right)

        return ans 
    
print(Solution().getSumAbsoluteDifferences(nums = [2,3,5])) # [4, 3, 5] 