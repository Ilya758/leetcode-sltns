class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        ans = float('inf')
        
        for num in nums:
            a, b = abs(num), abs(ans) 
            
            if a < b:
                ans = num
            elif a == b:
                ans = max(ans, num)

        return ans


print(Solution().findClosestNumber([-4,-2,1,4,8])) # 1