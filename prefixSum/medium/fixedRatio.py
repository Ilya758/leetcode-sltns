from typing import Counter


class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        ans = prefix = 0 
        freq = Counter({0 : 1})

        for c in s:
            prefix += num2 if c == '0' else -num1
            ans += freq[prefix]
            freq[prefix] += 1

        return ans 
    
print(Solution().fixedRatio(s = "0110011", num1 = 1, num2 = 2)) # 4