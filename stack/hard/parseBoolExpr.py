class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        ops = []
        stack = []

        def tokenize(token):
            return token == 't' if token in ['t', 'f'] else token

        for token in expression:
            if token in ['&', '!', '|']:
                ops.append(token)
            elif token == ')':
                result = stack[-1]
                op = ops[-1]

                while stack[-1] != '(':
                    last = stack[-1]

                    if op == '!':
                        result = not result
                    elif op == '|':
                        result = result or last
                    else:
                        result = result and last

                    stack.pop()

                stack.pop()
                stack.append(result)
                ops.pop()
            elif token != ',':
                stack.append(tokenize(token))

        return tokenize(stack[0])

print(Solution().parseBoolExpr("!(&(f,t))"))