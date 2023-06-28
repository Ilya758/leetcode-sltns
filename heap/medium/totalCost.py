
from heapq import *


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        left = 0
        right = n - 1
        ans = 0

        l = []
        r = []

        while candidates and left <= right:
            candidates -= 1
            l.append(costs[left])

            if left != right:
                r.append(costs[right])

            left += 1
            right -= 1

        heapify(l)
        heapify(r)

        while k and (l or r):
            a = heappop(l) if l else float('inf')
            b = heappop(r) if r else float('inf')

            if a < b or (a == b and left <= right):
                ans += a
                heappush(r, b)

                if left <= right:
                    heappush(l, costs[left])
                    left += 1

            else:
                ans += b
                heappush(l, a)

                if left <= right:
                    heappush(r, costs[right])
                    right -= 1

            k -= 1

        return ans


print(Solution().totalCost(costs=[31, 25, 72, 79, 74, 65, 84,
      91, 18, 59, 27, 9, 81, 33, 17, 58], k=11, candidates=2))  # 423
print(Solution().totalCost(
    costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4))  # 11
print(Solution().totalCost(
    costs=[1, 2, 4, 1], k=3, candidates=3
))  # 4
