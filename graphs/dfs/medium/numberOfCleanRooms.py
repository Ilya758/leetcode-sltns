class Solution:
    def numberOfCleanRooms(self, room: list[list[int]]) -> int:
        dirs = (0, 1, 0, -1, 0)
        n, m, = len(room), len(room[0])
        visited = set()
        cleaned = set()

        def dfs(row, col, direction):
            if (row, col, direction) in visited:
                return len(cleaned)

            visited.add((row, col, direction))
            cleaned.add((row, col))
            x = row + dirs[direction] 
            y = col + dirs[direction + 1]

            if 0 <= x < n and 0 <= y < m and not room[x][y]:
                return dfs(x, y, direction)

            return dfs(row, col, (direction + 1) % 4)

        return dfs(0, 0, 0)
    
print(Solution().numberOfCleanRooms([
    [0,0,0,1,0],
    [1,1,0,0,1],
    [1,1,0,0,1],
    [0,0,1,0,1],
    [1,1,0,1,0]])) # 5
