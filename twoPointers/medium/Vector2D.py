class Vector2D:

    def __init__(self, vec: list[list[int]]):
        self.i = self.j = 0
        self.vec = vec
        self.movePointers()

    def movePointers(self):
        while self.i != len(self.vec) and self.j == len(self.vec[self.i]):
            self.i += 1
            self.j = 0

    def next(self) -> int:
        vec = self.vec[self.i][self.j]
        self.j += 1
        self.movePointers()

        return vec

    def hasNext(self) -> bool:
        return self.i != len(self.vec)