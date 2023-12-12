class Solution:
    def totalNQueens(self, n: int) -> int:
        def bt(row, currD, antiD, cols):
            if row == n:
                return 1

            result = 0

            for col in range(n):
                cd, ad = row - col, row + col

                if col in cols or cd in currD or ad in antiD:
                    continue

                currD.add(cd)
                antiD.add(ad)
                cols.add(col)
                result += bt(row + 1, currD, antiD, cols)
                currD.remove(cd)
                antiD.remove(ad)
                cols.remove(col)

            return result

        return bt(0, set(), set(), set())

print(Solution().totalNQueens(n = 4)) # 2