from heapq import *


class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        heap = []
        n = len(arr)

        for i in range(n):
            heappush(heap, (arr[i] / arr[-1], i, n - 1))

        for _ in range(k - 1):
            cur = heappop(heap)
            a = cur[1]
            b = cur[2] - 1

            if b > a:
                heappush(heap, (arr[a] / arr[b], a, b))

        ans = heappop(heap)

        return [arr[ans[1]], arr[ans[2]]]
    
print(Solution().kthSmallestPrimeFraction(arr = [1,2,3,5], k = 3)) # [2,5]