class Solution:
    def check(self, nums: list[int]) -> bool:
        rotated = False
        curMax = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < nums[i - 1] and not rotated:
                rotated = True

                if num > nums[0]:
                    return False
            elif rotated and (num > curMax or num < nums[i - 1] or num > nums[0]): 
                return False

            curMax = max(curMax, num)
                
        return True
    
print(Solution().check([2,4,1,3])) # False