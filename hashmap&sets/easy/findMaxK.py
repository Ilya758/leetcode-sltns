class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        cache = set(nums)
        ans = -1

        for num in nums:
            if -num in cache and num > ans: ans = num
    
        return ans
    
print(Solution().findMaxK(nums = [-1,2,-3,3])) # 3 