class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        stack = []
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            cur = 0

            while stack and stack[-1] < heights[i]:
                stack.pop()
                cur += 1

            ans[i] = cur + int(len(stack) > 0)
            stack.append(heights[i])

        return ans
    
print(Solution().canSeePersonsCount([5,1,2,3,10])) # [4,1,1,1,0]