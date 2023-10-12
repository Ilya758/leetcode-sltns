class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(opened, closed, path):
            if opened + closed == 2 * n:
                ans.append("".join(path))
                return

            if opened != n: 
                path.append('(')
                backtrack(opened + 1, closed, path)
                path.pop()

            if opened > closed:
                path.append(')')
                backtrack(opened, closed + 1, path)
                path.pop()

        backtrack(1, 0, ['('])

        return ans

print(Solution().generateParenthesis(n=3)) # ["((()))","(()())","(())()","()(())","()()()"]