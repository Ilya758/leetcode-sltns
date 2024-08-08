class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        middle = [[0] * 10 for _ in range(10)]
        middle[1][3] = middle[3][1] = 2
        middle[1][7] = middle[7][1] = 4
        middle[3][9] = middle[9][3] = 6
        middle[7][9] = middle[9][7] = 8
        middle[1][9] = middle[9][1] = 5
        middle[3][7] = middle[7][3] = 5
        middle[2][8] = middle[8][2] = 5
        middle[4][6] = middle[6][4] = 5
        ans = 0

        def bt(prev, seen):
            nonlocal ans

            if len(seen) >= m:
                ans += 1

                if len(seen) == n:
                    return

            for i in range(1, 10):
                if i not in seen and (middle[prev][i] == 0 or middle[prev][i] in seen):
                    seen.add(i)
                    bt(i, seen)
                    seen.remove(i)

        for i in range(1, 10):
            bt(i, {i})

        return ans

print(Solution().numberOfPatterns(1, 2)) # 65