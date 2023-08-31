from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.q = deque()

    def pushFront(self, val: int) -> None:
        self.q.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        n = len(self.q) // 2
        self.q.insert(n, val)

    def pushBack(self, val: int) -> None:
        self.q.append(val)

    def popFront(self) -> int:
        return self.q.popleft() if self.q else - 1

    def popMiddle(self) -> int:
        if self.q:
            n = len(self.q)
            i = n // 2 - 1 if n % 2 == 0 else n // 2
            val = self.q[i]
            del self.q[i]

            return val

        return -1

    def popBack(self) -> int:
        return self.q.pop() if self.q else - 1