# https://leetcode.com/problems/valid-sudoku/description/

from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sq = defaultdict(set)

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell != '.':
                    if cell in rows[i] or cell in cols[j] or cell in sq[(i // 3, j // 3)]:
                        return False

                    rows[i].add(cell)
                    cols[j].add(cell)
                    sq[(i // 3, j // 3)].add(cell)

        return True


print(Solution().isValidSudoku(board=[
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))  # True
