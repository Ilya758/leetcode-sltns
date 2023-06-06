class Solution:
    def checkStraightLine(self, coords: list[list[int]]) -> bool:
        def getDiff(a, b):
            lx, ly = a
            rx, ry = b

            return lambda x, y: (x - lx) * (ry - ly) == (y - ly) * (rx - lx)

        equation = getDiff(coords[0], coords[-1])

        for i in range(1, len(coords) - 1):
            x, y = coords[i]
            if not equation(x, y):
                return False

        return True


print(Solution().checkStraightLine(coordinates=[
      [1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))  # false
