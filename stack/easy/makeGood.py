class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]

        for i in range(1, len(s)):
            c = s[i]
            last = stack[-1] if stack else None

            if last and c != last and c.upper() == last.upper():
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)


print(Solution().makeGood("abBAcC")) # ""