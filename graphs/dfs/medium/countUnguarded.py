class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        W = set(map(tuple, walls))
        G = set(map(tuple, guards))
        guarded = set()

        def dfs(row, col, dx, dy):
            while 0 <= row < m and 0 <= col < n and (row, col) not in W and (row, col) not in G:
                guarded.add((row, col))
                row += dx
                col += dy

        for row, col in guards:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(row + dx, col + dy, dx, dy)

        return m * n - len(guarded) - len(W) - len(G)


print(Solution().countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]])) # 7