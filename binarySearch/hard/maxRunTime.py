class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        left, right = 0, sum(batteries) // n

        while left <= right:
            mid = (left + right) >> 1
            total = 0

            for p in batteries:
                total += min(p, mid)

            if total // n >= mid:
                left = mid + 1
            else:
                right = mid - 1

        return right

print(Solution().maxRunTime(3, [10, 10, 3, 5])) # 8