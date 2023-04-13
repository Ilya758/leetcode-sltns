# https://leetcode.com/problems/validate-stack-sequences/

def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:
    left = 0
    right = 0
    stack: list[int] = []

    while (right < len(pushed)):
        stack.append(pushed[right])

        while len(stack) and stack[-1] == popped[left]:
            stack.pop()
            left += 1

        right += 1

    return not len(stack)


print(validateStackSequences(
    pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))  # True
print(validateStackSequences(
    pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))  # False
