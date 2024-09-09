class Solution:
    def findPattern(self, grid: list[list[int]], pattern: list[str]) -> list[int]:
        n, m = len(grid), len(grid[0])
        nN, mN = len(pattern), len(pattern[0])

        def check(i, j):
            char_to_digit = {}
            digit_to_char = {}

            for x in range(nN):
                for y in range(mN):
                    cell, p = grid[i + x][j + y], pattern[x][y]

                    if p.isdigit():
                        if int(p) != cell:
                            return False
                    else:
                        if p in char_to_digit and char_to_digit[p] != cell:
                            return False
                        elif cell in digit_to_char and digit_to_char[cell] != p:
                            return False
                            
                        char_to_digit[p] = cell
                        digit_to_char[cell] = p

            return True

        for i in range(n - nN + 1):
            for j in range(m - mN + 1):
                if check(i, j):
                    return [i, j]

        return [-1, -1]

    
print(Solution().findPattern(grid = [[1,2,2],[2,2,3],[2,3,3]], pattern = ["ab","bb"])) # [0, 0]