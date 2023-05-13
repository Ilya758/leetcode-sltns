# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, h: list[int]) -> int:
        left = 0
        right = len(h) - 1
        ans = float('-inf')

        while left <= right:
            curMin = min(h[left], h[right])

            # we only need to consider the lowest boundary
            # and then we'll fill
            # the container with water
            # by calculating size of sliding window
            ans = max(ans, curMin * (right - left))

            if h[left] < h[right]:
                left += 1
            else:
                right -= 1

        return ans


print(Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
