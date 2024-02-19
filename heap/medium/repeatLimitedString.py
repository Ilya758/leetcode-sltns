from collections import Counter
from heapq import *


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str: 
        heap = [(-ord(key), value) for key, value in Counter(s).items()]
        heapify(heap)
        ans = ""

        while heap:
            k, v = heappop(heap)

            if v <= repeatLimit:
                ans += chr(-k) * v
            else:
                ans += chr(-k) * repeatLimit

                if not heap:
                    break

                nextK, nextV = heappop(heap)
                ans += chr(-nextK)

                if nextV > 1:
                    heappush(heap, (nextK, nextV - 1))

                heappush(heap, (k, v - repeatLimit))

        return ans
    
print(Solution().repeatLimitedString(s = "aababab", repeatLimit = 2)) # bbabaa