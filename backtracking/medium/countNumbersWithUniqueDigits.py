class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def bt(path):
            res = 1

            for i in range(10):
                if i not in path:     
                    if len(path) < n:
                        path.add(i)
                        res += bt(path)
                        path.remove(i)

            return res

        return sum(bt({i}) for i in range(1, 10) if n) + 1

print(Solution().countNumbersWithUniqueDigits(2)) # 91