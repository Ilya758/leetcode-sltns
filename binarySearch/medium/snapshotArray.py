class SnapshotArray:
    snap_id = 0

    def __init__(self, length: int):
        self.snapshot = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.snapshot[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1

        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snapshot = self.snapshot[index]

        left = 0
        right = len(snapshot) - 1

        while left <= right:
            mid = (left + right) // 2
            snapId, _ = snapshot[mid]

            if snapId <= snap_id:
                left = mid + 1
            else:
                right = mid - 1

        return self.snapshot[index][left - 1][1]


s = SnapshotArray(1)
s.set(0, 4)
s.set(0, 16)
s.set(0, 13)
s.snap()
print(s.get(0, 0))
s.snap()
