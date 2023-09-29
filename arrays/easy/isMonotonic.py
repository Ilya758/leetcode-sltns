class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        isAscending = None

        for i in range(1, len(nums)):
            prev = nums[i - 1]

            if prev == nums[i]: continue

            if isAscending == None:
                isAscending = prev < nums[i]
            else:
                if (isAscending and prev > nums[i]) or (not isAscending and prev < nums[i]) :
                    return False
        
        return True
    
print(Solution().isMonotonic(nums = [6,5,4,4])) # True