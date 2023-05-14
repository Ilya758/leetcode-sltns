# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        def search(arr, target):
            l = 0
            r = len(arr) - 1

            while l <= r:
                mid = (l + r) // 2

                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return l

        potions.sort()

        ans = []
        n = len(potions)

        for spell in spells:
            i = search(potions, success / spell)
            ans.append(n - i)

        return ans


print(Solution().successfulPairs(
    spells=[5, 1, 3],
    potions=[1, 2, 3, 4, 5],
    success=7))  # [4, 0, 3]
