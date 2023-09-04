class Solution:
    def minSwaps(self, s: str) -> int:
        end = len(s) - 1
        stack = 0
        ans = 0

        for start in range(end):
            if s[start] == '[':
                stack += 1
            elif stack:
                stack -= 1
            else:
                ans += 1

                while s[end] != '[':
                    end -= 1

                stack += 1
                end -= 1

        return ans
    
print(Solution().minSwaps(s = "]]][[[")) # 2 