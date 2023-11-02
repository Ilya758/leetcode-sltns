class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        prefix = [nums[0]]
        n = len(nums)

        for i in range(1, n): prefix.append(prefix[i - 1] + nums[i])

        ans = []
        
        for i in range(len(nums)):
            before = nums[i] * i - prefix[i]
            after = - (prefix[i - 1] if i else 0) + prefix[n - 1] - nums[i] * (n - i - 1)
            ans.append(before + after)

        return ans 
    
print(Solution().getSumAbsoluteDifferences(nums = [2,3,5])) # [4, 3, 5] 