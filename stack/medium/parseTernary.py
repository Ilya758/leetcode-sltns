class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []

        for token in expression[::-1]:
            if stack and stack[-1] == '?':
                stack.pop()
                T, _, F = stack.pop(), stack.pop(), stack.pop()
                stack.append(T if token == 'T' else F)
            else:
                stack.append(token)

        return stack[0]
        

print(Solution().parseTernary("F?1:0"))