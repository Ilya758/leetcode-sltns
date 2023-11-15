from heapq import *

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        heapify(arr)
        prev = min(1, heappop(arr))

        while arr:
            prev = prev + 1 if arr[0] - prev else arr[0]
            heappop(arr)

        return prev
    
print(Solution().maximumElementAfterDecrementingAndRearranging(arr = [2,2,1,2,1]))