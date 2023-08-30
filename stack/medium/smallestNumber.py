class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        ans = []

        for i in range(len(pattern) + 1):
            stack.append(i + 1)

            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    ans.append(str(stack.pop()))

        return ''.join(ans)
    
print(Solution().smallestNumber(pattern='IIIDIDDD')) # 123549876
