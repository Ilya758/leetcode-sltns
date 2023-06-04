# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = str(bin(i)).count('1')

        return ans


print(Solution().countBits(n=5))  # [0,1,1,2,1,2]
