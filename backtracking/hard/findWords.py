class Solution:
    def findWords(self, grid: list[list[str]], words: list[str]) -> list[str]:
        trie = {}
        key = '$'
        n, m = len(grid), len(grid[0])

        for w in words:
            node = trie

            for ch in w:
                if ch not in node:
                    node[ch] = {}

                node = node[ch]

            node[key] = w

        def isValid(row, col):
            return 0 <= row < n and 0 <= col < m

        ans = []
        
        def bt(row, col, parent):
            ch = grid[row][col]
            curNode = parent[ch]
            w = curNode.pop(key, False)
            
            if w:
                ans.append(w)

            grid[row][col] = '#'

            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                x, y = row + dx, col + dy

                if isValid(x, y) and grid[x][y] in curNode:
                    bt(row + dx, col + dy, curNode)

            grid[row][col] = ch
            
            if not curNode:
                parent.pop(ch)


        for i in range(n):
            for j in range(m):
                if grid[i][j] in trie:
                    bt(i, j, trie)

        return ans

print(Solution().findWords(grid =
[["a","b"],["c","d"]], words =
["abcb"])) # []