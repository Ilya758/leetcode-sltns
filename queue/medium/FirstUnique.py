from collections import defaultdict, deque


class FirstUnique:

    def __init__(self, nums: list[int]):
        self.cache = defaultdict(int)
        self.q = deque([])

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        self.cache[value] += 1
        self.q.append(value)

        while self.q and self.cache[self.q[0]] > 1:
            self.q.popleft()