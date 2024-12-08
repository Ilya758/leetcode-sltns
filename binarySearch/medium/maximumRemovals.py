class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        left, right = 0, len(removable)
        n, m = len(s), len(p)

        def check(x):
            seen = set(removable[:x])
            i, j = 0, 0

            while i < n and j < m:
                if i not in seen:
                    if s[i] == p[j]:
                        j += 1

                i += 1

            return j == m

        while left < right:
            mid = (left + right + 1) // 2

            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left


print(Solution().maximumRemovals(s = "abcacb", p = "ab", removable = [3,1,0])) # 2