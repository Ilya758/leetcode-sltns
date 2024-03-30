from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def calc(x):
            cur = 0
            cache = defaultdict(int)
            i = 0

            for j in range(len(nums)):
                cache[nums[j]] += 1

                while i <= j and len(cache) > x:
                    cache[nums[i]] -= 1

                    if not cache[nums[i]]:
                        del cache[nums[i]]

                    i += 1

                cur += j - i + 1
                
            return cur

        return calc(k) - calc(k - 1)

print(Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2)) # 7