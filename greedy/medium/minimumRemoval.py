# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/description/

class Solution:
    def minimumRemoval(self, beans: list[int]) -> int:
        ans = float('inf')
        s = sum(beans)
        n = len(beans)
        beans.sort()

        for i in range(n):
            ans = min(ans, s - (n - i) * beans[i])

        return ans


print(Solution().minimumRemoval(beans=[4, 1, 6, 5]))  # 4
print(Solution().minimumRemoval(beans=[2, 10, 3, 2]))  # 7
