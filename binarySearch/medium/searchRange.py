class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def search(isLeft = True):
            left, right = 0, len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    index = mid

                    if isLeft:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                
            return index
        
        return [search(), search(False)]

print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8)) # [3, 4]