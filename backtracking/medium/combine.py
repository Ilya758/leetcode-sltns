# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(curr: list[int] = [], i=1):
            if len(curr) == k:
                ans.append(curr[:])

                return

            for j in range(i, n + 1):
                curr.append(j)
                backtrack(curr, j + 1)
                curr.pop()

        ans = []

        backtrack()

        return ans


print(Solution().combine(n=4, k=2))  # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
