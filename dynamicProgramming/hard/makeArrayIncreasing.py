import bisect
from functools import cache


class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2 = sorted(set(arr2))

        @cache
        def dp(i, prev):
            if i == len(arr1):
                return 0

            skip = float("inf")
            replace = float("inf")

            if arr1[i] > prev:
                skip = dp(i + 1, arr1[i])

            idx = bisect.bisect_right(arr2, prev)

            if idx < len(arr2):
                replace = 1 + dp(i + 1, arr2[idx])

            return min(skip, replace)

        ans = dp(0, float("-inf"))

        return -1 if ans == float("inf") else ans


print(Solution().makeArrayIncreasing(arr1=[4, 2, 3], arr2=[6, 5]))  # 2
print(Solution().makeArrayIncreasing(
    arr1=[1, 5, 3, 6, 7], arr2=[4, 3, 1]))  # 2
print(Solution().makeArrayIncreasing(
    arr1=[1, 5, 3, 6, 7], arr2=[1, 6, 3, 3]))  # -1
