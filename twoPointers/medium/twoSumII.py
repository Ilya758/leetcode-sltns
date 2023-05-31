# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left <= right:
            s = nums[left] + nums[right]
            if s == target:
                return [left + 1, right + 1]
            elif s > target:
                right -= 1
            else:
                left += 1


print(Solution().twoSum(numbers=[2, 7, 11, 15], target=9))  # [1, 2]
