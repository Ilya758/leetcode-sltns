from heapq import *


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        for ast in sorted(asteroids):
            if ast > mass:
                return False

            mass += ast

        return True


print(Solution().asteroidsDestroyed(
    mass=10, asteroids=[3, 9, 19, 5, 21]))  # True
print(Solution().asteroidsDestroyed(mass=5, asteroids=[4, 9, 23, 4]))  # False
