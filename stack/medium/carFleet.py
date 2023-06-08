class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # 1. associate position and car speed
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []

        # 2. start iterate in sorted reverse order
        for p, s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)

            # 3. we carry about the last car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


print(Solution().carFleet(target=12, position=[
      10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))  # 3
