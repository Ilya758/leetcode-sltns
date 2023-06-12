# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        self.ans = 0

        def binarySearch(nums):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1

            self.ans += len(nums) - left

        for row in grid:
            binarySearch(row)

        return self.ans


print(Solution().countNegatives(
    grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))  # 8
