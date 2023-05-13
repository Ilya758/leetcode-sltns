# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = [''] * n

        while n >= 1:
            if k - 26 >= n:
                k -= 26
                ans[n - 1] = 'z'
            else:
                ans[n - 1] = chr(97 + k - n)
                k = n - 1

            n -= 1

        return ''.join(ans)


print(Solution().getSmallestString(n=5, k=73))  # "aaszz"
