# https://leetcode.com/problems/knight-probability-in-chessboard/description/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # in chessboard a knight can move in 8 directions
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                      (2, 1), (2, -1), (-2, 1), (-2, -1)]

        # initialize cache with k moves in matrix
        dp = [[[-1] * n for _ in range(n)] for _ in range(k + 1)]

        def calculate_dp(moves, i, j):
            # any time we're out of moves
            if moves == 0:
                # check, if we land to the starting cell
                if i == row and j == column:
                    return 1
                else:
                    return 0

            # use the cache
            if dp[moves][i][j] != -1:
                return dp[moves][i][j]

            dp[moves][i][j] = 0

            # traverse in all directions
            for direction in directions:
                prev_i = i - direction[0]
                prev_j = j - direction[1]

                #  and check if knight is still on board
                if 0 <= prev_i < n and 0 <= prev_j < n:
                    dp[moves][i][j] += calculate_dp(moves - 1, prev_i, prev_j)

            dp[moves][i][j] /= 8

            return dp[moves][i][j]

        # iterate over all cells in matrix
        total_probability = sum(
            calculate_dp(k, i, j)
            for i in range(n)
            for j in range(n)
        )

        return total_probability


print(Solution().knightProbability(n=3, k=2, row=0, column=0))  # 0.0625
print(Solution().knightProbability(n=1, k=0, row=0, column=0))  # 1
