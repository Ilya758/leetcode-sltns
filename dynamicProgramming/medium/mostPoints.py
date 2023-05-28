from functools import cache


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        @cache
        def dp(i):
            if i >= len(questions):
                return 0

            j = i + questions[i][1] + 1

            return max(questions[i][0] + dp(j), dp(i + 1))

        return dp(0)


print(Solution().mostPoints(questions=[[3, 2], [4, 3], [4, 4], [2, 5]]))  # 5
