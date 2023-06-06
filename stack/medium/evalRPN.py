class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        stack = []

        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](int(a), int(b)))

        return int(stack[0])


print(Solution().evalRPN(tokens=[
      "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
