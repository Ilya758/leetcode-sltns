class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        ans = float('inf')
        distribution = [0] * k

        def backtrack(i):
            nonlocal ans

            if i == len(cookies):
                ans = min(ans, max(distribution))
                return

            if ans <= max(distribution):
                return

            for j in range(k):
                distribution[j] += cookies[i]
                backtrack(i + 1)
                distribution[j] -= cookies[i]

        backtrack(0)

        return ans


print(Solution().distributeCookies(cookies=[8, 15, 10, 20, 8], k=2))  # 31
print(Solution().distributeCookies(cookies=[6, 1, 3, 2, 2, 4, 1, 2], k=3))  # 7
print(Solution().distributeCookies(cookies=[13, 3],  k=2,))  # 13
