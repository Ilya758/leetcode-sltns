class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        ans = 1
        k -= 1

        def get(a, b):
            res = 0

            while a <= n:
                res += min(n + 1, b) - a
                a *= 10
                b *= 10

            return res

        while k:
            steps = get(ans, ans + 1)

            if steps <= k:
                k -= steps
                ans += 1
            else:
                ans *= 10
                k -= 1

        return ans
    
print(Solution().findKthNumber(13, 2)) # 10
