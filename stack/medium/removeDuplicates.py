class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        counter = []

        for char in s:
            if not stack or stack[-1] != char:
                stack.append(char)
                counter.append(1)
            else:
                counter[-1] += 1

                if counter[-1] == k:
                    stack.pop()
                    counter.pop()

        return ''.join([v * k for k, v in zip(stack, counter)])
    
print(Solution().removeDuplicates('abcd', 2)) # abcd