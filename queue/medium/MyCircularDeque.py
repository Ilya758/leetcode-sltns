from collections import deque


class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = deque()
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque.appendleft(value)
            return True

        return False 

    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque.append(value)
            return True

        return False

    def deleteFront(self) -> bool:
        if len(self.deque):
            self.deque.popleft()
            return True

        return False

    def deleteLast(self) -> bool:
        if len(self.deque):
            self.deque.pop()
            return True

        return False

    def getFront(self) -> int:
        return self.deque[0] if len(self.deque) else -1

    def getRear(self) -> int:
        return self.deque[-1] if len(self.deque) else -1

    def isEmpty(self) -> bool:
        return not len(self.deque)

    def isFull(self) -> bool:
        return len(self.deque) == self.k