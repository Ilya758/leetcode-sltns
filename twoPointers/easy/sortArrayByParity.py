class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if not nums[left] % 2:
                left += 1
                continue
            
            if nums[right] % 2:
                right -= 1
                continue

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
    
print(Solution().sortArrayByParity(nums = [3,1,2,4])) # [2,4,3,1]