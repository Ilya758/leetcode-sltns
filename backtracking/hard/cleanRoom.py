class Solution:
    def cleanRoom(self, robot):
        seen = {(0, 0)}
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def returnBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def bt(row, col, d):
            robot.clean()

            for _ in range(4):
                new_d = (d + _) % 4
                dx, dy = dirs[new_d]
                x, y = row + dx, col + dy

                if (x, y) not in seen and robot.move():
                    seen.add((row, col))
                    bt(x, y, new_d)
                    returnBack()

                robot.turnRight()

        bt(0, 0, 0)
