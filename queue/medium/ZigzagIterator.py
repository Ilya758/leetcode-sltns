from collections import deque


class ZigzagIterator:
    def __init__(self, v1: list[int], v2: list[int]):
        i = 0
        self.vals = deque([])

        while i < len(v1) or i < len(v2):
            if i < len(v1):
                self.vals.append(v1[i])
            if i < len(v2):
                self.vals.append(v2[i])
            
            i += 1

    def next(self) -> int:
        return self.vals.popleft()

    def hasNext(self) -> bool:
        return len(self.vals) > 0
