class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        n = len(position)

        def check(k):
            res = 1
            prev = 0

            for i in range(1, n):
                if position[i] - position[prev] >= k:
                    prev = i
                    res += 1

            return res >= m


        while left <= right:
            mid = (left + right) >> 1

            if check(mid): left = mid + 1
            else: right = mid - 1

        return left - 1

print(Solution().maxDistance([1,2,3,4,7], 3)) # 3