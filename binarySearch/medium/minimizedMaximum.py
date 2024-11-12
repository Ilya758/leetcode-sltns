from math import ceil


class Solution:
    def minimizedMaximum(self, n: int, A: list[int]) -> int:
        left, right = 1, max(A)

        def check(x):
            res = 0

            for q in A:
                res += ceil(q / x)

                if res > n:
                    return False

            return True


        while left < right:
            mid = (left + right) >> 1

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

print(Solution().minimizedMaximum(7, [15, 10, 10])) # 5