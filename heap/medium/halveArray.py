from heapq import *


def halveArray(nums: list[int]) -> int:
    target = sum(nums) / 2
    heap = [-num for num in nums]
    heapify(heap)
    ans = 0

    while target > 0:
        ans += 1
        num = heappop(heap) / 2
        target += num
        heappush(heap, num)

    return ans


print(halveArray(nums=[5, 19, 8, 1]))  # 3
