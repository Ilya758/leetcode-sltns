class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        ans = 0
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        n, m = len(board), len(board[0])

        def isValid(row, col):
            return 0 <= row < n and 0 <= col < m

        for row in range(n):
            for col in range(m):
                if board[row][col] == 'R':
                    for dx, dy in dirs:
                        x, y = row + dx, col + dy

                        while isValid(x, y):
                            if board[x][y] == 'p':
                                ans += 1
                                break
                            if board[x][y] == 'B':
                                break
                            
                            x += dx
                            y += dy

        return ans 
    
print(Solution().numRookCaptures(board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
))