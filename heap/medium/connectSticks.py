from heapq import *


def connectSticks(sticks: list[int]) -> int:
    heapify(sticks)
    ans = 0

    while len(sticks) > 1:
        a = heappop(sticks)
        b = heappop(sticks)
        ans += a+b
        heappush(sticks, a + b)

    return ans


print(connectSticks(sticks=[2, 4, 3]))  # 14
