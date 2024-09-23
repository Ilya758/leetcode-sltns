from collections import deque


class SnakeGame:
    def __init__(self, width: int, height: int, food: list[list[int]]):
        self.m = width
        self.n = height
        self.food = deque(food)
        self.snake = deque([(0, 0)])
        self.moves = set([(0, 0)])

    def isValid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m

    def move(self, direction: str) -> int:
        row, col = self.snake[0]
        x, y = (row + (direction == 'D') - (direction == 'U'),
                col + (direction == 'R') - (direction == 'L'))

        if not self.isValid(x, y) or ((x, y) in self.moves and (x, y) != self.snake[-1]):
            return -1

        if self.food and self.food[0] == [x, y]:
            self.food.popleft()
        else:
            self.moves.remove(self.snake.pop())

        self.snake.appendleft((x, y))
        self.moves.add((x, y))

        return len(self.snake) - 1

s = SnakeGame(3, 2, [[1, 2], [0, 1]])
print(s.move('R')) # 0
print(s.move('D')) # 0
print(s.move('R')) # 1 
print(s.move('U')) # 1
print(s.move('L')) # 2
print(s.move('U')) # -1