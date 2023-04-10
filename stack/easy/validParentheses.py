# https://leetcode.com/problems/valid-parentheses/description/

def isValid(s: str) -> bool:
    stack = []
    pars = {'(': ')', '{': '}', "[": "]"}

    for char in s:
        if char in pars:
            stack.append(char)
        else:
            if not len(stack):
                return False

            top = stack.pop()

            if (char != pars[top]):
                return False

    return not len(stack)


print(isValid(s="()[]{}"))  # true
print(isValid(s="(]"))  # false
