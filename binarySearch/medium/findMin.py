class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
                
print(Solution().findMin([3,1,2])) # 1