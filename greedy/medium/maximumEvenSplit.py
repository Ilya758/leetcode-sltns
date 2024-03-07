class Solution:
    def maximumEvenSplit(self, f: int) -> list[int]:
        ans, i = [], 2

        if f % 2 == 0:
            while i <= f:
                ans.append(i)
                f -= i
                i += 2

            ans[-1] += f

        return ans

print(Solution().maximumEvenSplit(14))