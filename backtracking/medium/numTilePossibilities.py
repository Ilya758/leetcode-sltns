from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        map = Counter(tiles)
            
        def bt(path):
            c = 0

            for i in map:
                if map[i]:
                    map[i] -= 1
                    path += i
                    c += 1 + bt(path)
                    map[i] += 1
            
            return c

        return bt('')

print(Solution().numTilePossibilities('AAABBC')) # 188