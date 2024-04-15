class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        stack = []

        for v in arr:
            if stack and stack[-1] > v:
                curMax = stack[-1]

                while stack and stack[-1] > v:
                    stack.pop()

                stack.append(curMax)
            else:
                stack.append(v)

        return len(stack)

print(Solution().maxChunksToSorted([5, 4, 3, 2, 1])) # 