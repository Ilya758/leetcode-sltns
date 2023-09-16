class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        j = 0

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None
            else:
                if nums[j] == None:
                    nums[j] = nums[i]
                    nums[i] = None
                
                j += 1

        return j
    

print(Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
