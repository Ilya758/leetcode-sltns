from heapq import *


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        idx = 1
        heap = []
        heapify(heap)

        while idx < len(heights):
            prev, cur = heights[idx - 1], heights[idx]
            diff = cur - prev
            
            if diff > 0:
                heappush(heap, diff) 

                if len(heap) > ladders:
                    lowest = heappop(heap)

                    if lowest > bricks:
                        break
                        
                    bricks -= lowest
            
            idx += 1
                
        return idx - 1

print(Solution().furthestBuilding(heights =
[1,5,1,2,3,4,10000],
bricks =
4,
ladders =
1)) # 5
