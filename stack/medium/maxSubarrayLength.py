class Solution:
    def maxSubarrayLength(self, nums: list[int]) -> int:
        ans, n = 0, len(nums)
        stack = []

        for i in range(n - 1, -1, -1):
            if not stack or nums[i] < nums[stack[-1]]: 
                stack.append(i)

        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]: 
                ans = max(ans, stack.pop() - i + 1)
        
        return ans
    
print(Solution().maxSubarrayLength(nums = [7,6,5,4,3,2,1,6,10,11])) # 8