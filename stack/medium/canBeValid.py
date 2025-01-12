class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open = []
        free = []

        for i, char in enumerate(s):
            if locked[i] == '0':
                free.append(i)
            elif char == '(':
                open.append(i)
            elif open:
                open.pop()
            elif free:
                free.pop()
            else:
                return False

        while open and free:
            if open[-1] > free[-1]:
                return False
                
            open.pop()
            free.pop()

        return not open

print(Solution().canBeValid("((()(()()))()((()()))))()((()(()", "10111100100101001110100010001001")) # True

