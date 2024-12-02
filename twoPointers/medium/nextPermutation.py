class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i != -1:
            j = n - 1
            
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]

        i += 1
        j = n - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
            i += 1
        
print(Solution().nextPermutation([1,2,3])) # 132