# https://leetcode.com/problems/asteroid-collision/description/

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        # since we treat this problem as a stack problem
        # first initialize stack with the first asteroid
        stack = [asteroids[0]]

        # how do we check if asteroids cannot collide?
        # 1) they're moving in the same direction (1 and 2)
        # 2) they're moving in different sides
        # (consider this) =>
        # <-2 2-> (True) and 2-> <-2 (False)
        def cannotCollide(a, b):
            return (a >= 0 and b >= 0) or (a < 0 and b < 0) or (a < 0 and b >= 0)

        for i in range(1, len(asteroids)):
            cur = asteroids[i]

            if not stack or cannotCollide(stack[-1], cur):
                stack.append(cur)
            else:
                destroyed = False
                acur = abs(cur)

                # any time the asteroids can collide to each other
                while len(stack) and stack[-1] >= 0:
                    ap = abs(stack[-1])

                    # if the last has the bigger mass, the current is destroyed
                    if ap > acur:
                        destroyed = True
                        break
                    # otherwise destroy the last and continue
                    elif ap < acur:
                        stack.pop()
                    # they destroyed both
                    else:
                        destroyed = True
                        stack.pop()
                        break

                if not destroyed:
                    stack.append(cur)

        return stack


print(Solution().asteroidCollision(asteroids=[5, 10, -5]))  # [5, 10]
print(Solution().asteroidCollision(asteroids=[8, -8]))  # []
print(Solution().asteroidCollision(asteroids=[5, 10, -12]))  # [-12]
