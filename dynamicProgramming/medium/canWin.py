from functools import cache


class Solution:
    def canWin(self, currentState: str) -> bool:
        @cache
        def dp(state):
            for i in range(len(state) - 1):
                if state[i] == state[i + 1] == '+':
                    if not dp(state[:i] + '--' + state[i+2:]):
                        return True

            return False

        return dp(currentState)


print(Solution().canWin('++++')) # True