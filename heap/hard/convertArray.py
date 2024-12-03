from heapq import *


class Solution:
    def convertArray(self, nums: list[int]) -> int:
        def calc(nums):
            res = 0
            heap = []

            for num in nums:
                if heap and num > heap[0]:
                    res += num - heappop(heap)
                    heappush(heap, num)

                heappush(heap, num)
            
            return res
        
        return min(calc(nums), calc(nums[::-1]))


print(Solution().convertArray([3,2,4,5,0]))


