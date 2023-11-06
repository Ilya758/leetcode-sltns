from heapq import *


class SeatManager:
    def __init__(self, n: int):
        self.heap = []
        self.idx = 0

    def reserve(self) -> int:
        if self.heap:
            return heappop(self.heap)

        self.idx += 1
        return self.idx

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.heap, seatNumber)