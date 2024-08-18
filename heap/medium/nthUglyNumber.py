from heapq import *


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        primes = [2, 3, 5]

        for _ in range(n - 1):
            current = heappop(heap)

            for prime in primes:
                new = current * prime

                if new not in seen:
                    seen.add(new)
                    heappush(heap, new)

        return heappop(heap)


print(Solution().nthUglyNumber(10)) # 12