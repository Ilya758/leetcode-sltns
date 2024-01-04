from collections import Counter


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        cache = Counter(nums)
        stack = list(cache.values())
        ans = 0
        
        while stack:
            v = stack.pop()
            d = v % 3

            if d == v == 1:
                return -1

            ans += v // 3 + int(d != 0)

        return ans

print(Solution().minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12])) # 7