class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        stack = []

        def backtrack(open, closed):
            if open == closed == n:
                ans.append("".join(stack))
                return

            if open < n:
                stack.append('(')
                backtrack(open + 1, closed)
                stack.pop()

            if closed < open:
                stack.append(')')
                backtrack(open, closed + 1)
                stack.pop()

        backtrack(0, 0)

        return ans


print(Solution().generateParenthesis(3))
# ["((()))","(()())","(())()","()(())","()()()"]
