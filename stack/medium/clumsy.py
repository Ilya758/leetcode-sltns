class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        x = 0

        for num in range(n - 1, 0, -1):
            if x == 0:
                stack.append(stack.pop() * num)
            elif x == 1:
                stack.append(stack.pop() // num)
            else:
                stack.append(num)

            x = (x + 1) % 4

        x = 0

        for i in range(1, len(stack)):
            if x:
                stack[i] = stack[i - 1] - stack[i]
            else:
                stack[i] += stack[i - 1]

            x ^= 1

        return stack[-1]
    
print(Solution().clumsy(10)) # 12