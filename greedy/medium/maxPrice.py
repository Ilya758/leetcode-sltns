from heapq import *


class Solution:
    def maxPrice(self, items: list[list[int]], capacity: int) -> float:
        ans = 0

        for _, p, w in sorted([[p / w, p, w] for p, w in items], reverse=True):
            count = min(capacity, w)
            ans += p * count / w
            capacity -= count
            

        return -1 if capacity else ans
    

print(Solution().maxPrice([[13,9],[7,19],[20,17],[19,1]], 16)) # 39.0588