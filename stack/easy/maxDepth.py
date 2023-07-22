# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        cur = 0
        stack = []

        for char in s:
            if char == '(':
                stack.append('(')
                cur += 1
            elif char == ')':
                stack.pop()
                ans = max(ans, cur)
                cur -= 1

        return ans


print(Solution().maxDepth(s="(1+(2*3)+((8)/4))+1"))  # 3
print(Solution().maxDepth(s="(1)+((2))+(((3)))"))  # 3
