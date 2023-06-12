# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        ans = 0
        # 1. consider of using monotonic stack,
        # where each new pair == (index, height).
        # index is the positive number, the position, where it can extend from
        # and height is the current value for possible extension
        stack = []

        for i, h in enumerate(heights):
            start = i

            # 2. every time the monotonic condition is broken
            # pop the value => update maximum => extend the index
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                ans = max(ans, height * (i - index))
                start = index

            stack.append((start, h))

        # 3. many cases leave non-empty stack,
        # the idea is to calculate extension for these values
        for i, h in stack:
            ans = max(ans, h * (len(heights) - i))

        return ans


print(Solution().largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))  # 10
print(Solution().largestRectangleArea(heights=[2, 1, 2]))  # 3
