from heapq import *

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        heapify(heap)
        ans = 0

        while len(heap) > 1:
            print('ere')
            first, sec = heappop(heap) + 1, heappop(heap) + 1
            ans += 1

            if first < 0: heappush(heap, first)
            if sec < 0: heappush(heap, sec)
            
        return ans

print(Solution().maximumScore(a = 4, b = 4, c = 6)) # 6