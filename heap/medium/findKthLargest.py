from heapq import *


def findKthLargest(nums: list[int], k: int) -> int:
    nums = [-num for num in nums]
    heapify(nums)
    ans = 0

    while k:
        k -= 1
        ans = -heappop(nums)

    return ans


print(nums=[3, 2, 1, 5, 6, 4], k=2)  # 5
