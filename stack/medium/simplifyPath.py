def simplifyPath(path: str) -> str:
    s = list(filter(lambda x: x, path.split('/')))
    stack = []

    for i in range(len(s)):
        if s[i] == '..':
            if (len(stack)):
                stack.pop()
        elif s[i] != '.':
            stack.append(s[i])

    return '/' + '/'.join(stack) if len(stack) else '/'


print(simplifyPath("/home/"))  # /home
print(simplifyPath("/home//foo/"))  # "/home/foo"
