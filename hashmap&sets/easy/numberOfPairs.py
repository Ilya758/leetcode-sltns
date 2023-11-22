from collections import defaultdict


class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        cache = defaultdict(int)
        pairs = 0

        for num in nums:
            cache[num] += 1

            if cache[num] % 2 == 0:
                pairs += 1        

        return [pairs, len(nums) - pairs * 2]
    
print(Solution().numberOfPairs(nums = [1,3,2,1,3,2,2])) # [3,1] 