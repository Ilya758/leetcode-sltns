# https://leetcode.com/problems/trapping-rain-water/description/

class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        # 1. store max values from left and right
        leftMax = 0
        rightMax = 0
        ans = 0

        # 2. we need the rule, that helps us to shift indices
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    ans += leftMax - height[left]

                left += 1
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    ans += rightMax - height[right]

                right -= 1

        return ans


print(Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
