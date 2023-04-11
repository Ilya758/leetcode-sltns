# https://leetcode.com/problems/removing-stars-from-a-string/description/

def removeStars(s: str) -> str:
    stack: list[str] = list()

    for _, char in enumerate(s):
        if char != '*':
            stack.append(char)
        else:
            stack.pop()

    return "".join(stack)


print(removeStars('leet**cod*e'))  # lecoe
print(removeStars('erase*****'))
