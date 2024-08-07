class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], add: int) -> int:
        ans = 0

        for bag in sorted([a - b for a, b in zip(capacity, rocks)]):
            if bag <= add:
                add -= bag
                ans += 1
            else:
                break

        return ans

print(Solution().maximumBags(capacity = [2,3,4,5], rocks = [1,2,4,4], add = 2)) # 3