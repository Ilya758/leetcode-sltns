from heapq import *


class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        n = len(quality)
        ans = float("inf")
        totalQuality = 0
        ratio = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)])
        workers = []

        for i in range(n):
            heappush(workers, -ratio[i][1])
            totalQuality += ratio[i][1]

            if len(workers) > k:
                totalQuality += heappop(workers)

            if len(workers) == k:
                ans = min(ans, totalQuality * ratio[i][0])

        return ans

print(Solution().mincostToHireWorkers(quality =
[3,1,10,10,1],
wage =
[4,8,2,2,7], k=3)) 