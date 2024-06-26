class Solution:
    def maximumLengthOfRanges(self, nums: list[int]) -> list[int]:
        stack = []
        n = len(nums)
        ans = [0] * n
        nums.append(float('inf'))
        
        for right in range(n+1):
            while stack and nums[stack[-1]] < nums[right]:
                idx = stack.pop()
                left = -1 if not stack else stack[-1]
                ans[idx] = right - left - 1

            stack.append(right)
        
        return ans
    
print(Solution().maximumLengthOfRanges([1,5,4,3,6])) # [1, 4, 2, 1, 5]